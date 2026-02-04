import os                   # For file path and environment variable handling
import pandas as pd         # For data manipulation with DataFrames
from flask import Flask, render_template_string

from data_quality.checker import check_not_null  # Custom function to check for nulls in columns
# from data_quality.notifier import send_email   # Only import if email notification is enabled

#from data_quality.mongodb.models import (
#    create_user, create_dataset, create_quality_report
#)

from data_quality.playwright_agent import fetch_html_playwright

URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

# Create example user and dataset
#user_id = create_user("alice", "alice@example.com")
#dataset_id = create_dataset("Test Data", "/path/to/sample.csv")

# After running your quality check...
column_checks = [{"column_name": "id", "null_count": 0},
                 {"column_name": "name", "null_count": 1}]
#report_id = create_quality_report(user_id, dataset_id, column_checks)
#print(f"Inserted report with id: {report_id}")

# =========================
# Configuration Parameters
# =========================
CSV_PATH = "sample.csv"                     # Path to the input CSV file
COLUMNS_TO_CHECK = ['id', 'name', 'age']    # Columns that must not contain nulls

def fetch_and_parse_table_with_playwright():
    html = fetch_html_playwright(URL)
    tables = pd.read_html(html)
    return tables[0]

def load_data(file_path):
    """
    Loads data from a CSV file into a Pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data.
    
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[load_data] File not found: {file_path}")
    return pd.read_csv(file_path)


def run_data_quality_checks(df, columns):
    """
    Checks for null values in specified columns of a DataFrame.
    
    Args:
        df (pd.DataFrame): Input data.
        columns (list of str): Columns to check for missing values.
    
    Returns:
        dict: Mapping from column name to count of nulls.
    
    Raises:
        ValueError: If any specified columns are not in the DataFrame.
    """
    # Identify columns that are missing from the DataFrame
    missing_cols = [col for col in columns if col not in df.columns]
    if missing_cols:
        raise ValueError(
            f"[run_data_quality_checks] Missing columns in the data: {missing_cols}"
        )
    return check_not_null(df, columns)


def format_report(report):
    """
    Formats the data quality report as a multi-line string.

    Args:
        report (dict): Column name to missing value count.

    Returns:
        str: Multi-line string report.
    """
    return "\n".join(f"{col}: {cnt}" for col, cnt in report.items())


def print_report(report, body):
    """
    Prints the data quality report in a clear tabular format.

    Args:
        report (dict): Column-null count dictionary.
        body (str): Multi-line pretty string.
    """
    print("\n=== Data Quality Report ===")
    # Table header
    print("{:<15} | {:>10} | {}".format("Column", "Missing", "Status"))
    print("-" * 40)

    all_good = True
    for col, cnt in report.items():
        status = "✅ OK" if cnt == 0 else f"⚠️  {cnt} missing"
        print("{:<15} | {:>10} | {}".format(col, cnt, status))
        if cnt != 0:
            all_good = False

    print("-" * 40)
    summary = "All columns are complete! 🎉" if all_good else "Some columns have missing values!"
    print(f"Summary: {summary}")
    print("==============================\n")

    print("Raw email body (for debugging or notification):")
    print(body)

def make_html(report, body):
    rows = ""
    for col, cnt in report.items():
        status = '✅ OK' if cnt == 0 else f'⚠️  {cnt} missing'
        color = 'green' if cnt == 0 else 'orange'
        rows += f"<tr><td>{col}</td><td>{cnt}</td><td style='color:{color};'>{status}</td></tr>"
    return f"""
    <html>
    <head><title>Data Quality Report</title></head>
    <body>
        <h2>Data Quality Report</h2>
        <table border=1>
            <tr><th>Column</th><th>Missing</th><th>Status</th></tr>
            {rows}
        </table>
        <br><pre>{body}</pre>
    </body>
    </html>
    """

def run_web_report(report, body, port=5000):
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template_string(make_html(report, body))

    print(f"Serving report at http://127.0.0.1:{port}/ ...")
    app.run(port=port)

def generate_html_report(report, body, filename="report.html"):
    html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Data Quality Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 2em; }
        table { border-collapse: collapse; width: 60%%; }
        th, td { border: 1px solid #cccccc; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .status-ok { color: green; font-weight: bold; }
        .status-warn { color: orange; font-weight: bold; }
    </style>
</head>
<body>
    <h2>Data Quality Report</h2>
    <table>
        <tr><th>Column</th><th>Missing</th><th>Status</th></tr>
"""
    all_good = True
    for col, cnt in report.items():
        status = '<span class="status-ok">OK ✅</span>' if cnt == 0 else f'<span class="status-warn">{cnt} missing ⚠️</span>'
        html += f"<tr><td>{col}</td><td>{cnt}</td><td>{status}</td></tr>\n"
        if cnt != 0:
            all_good = False

    summary = "<b>All columns are complete! 🎉</b>" if all_good else "<b>Some columns have missing values.</b>"
    html += f"""</table><br><div>{summary}</div><hr>
    <h4>Raw Report Body</h4>
    <pre>{body}</pre>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"HTML report saved as '{filename}'. Open this file in your browser.")

def main():
    df = fetch_and_parse_table_with_playwright()
    print(df.head())
    df.to_csv("country_population_playwright.csv", index=False)

    try:
        # 1. Load the source data
        df = load_data(CSV_PATH)

        # 2. Run quality checks on specified columns
        report = run_data_quality_checks(df, COLUMNS_TO_CHECK)

        # 3. Create a pretty-format string of the report
        body = format_report(report)

        # 4. Print to console (or optionally, send by email)
        print_report(report, body)

        # 5. (Optional) Email the report - Enable and configure if needed!
        # send_email(
        #     subject="Data Quality Report",
        #     body=body,
        #     recipients=['email@epam.com'],
        #     smtp_server=os.getenv("SMTP_SERVER"),
        #     smtp_port=int(os.getenv("SMTP_PORT", 465)),
        #     sender=os.getenv("EMAIL_USERNAME"),
        #     password=os.getenv("EMAIL_PASSWORD")
        # )

	# 6. Create an html page
        generate_html_report(report, body)

        # ...in your main()...
        run_web_report(report, body)

    except Exception as e:
        print(f"[main] Error: {e}")


if __name__ == "__main__":
    main()