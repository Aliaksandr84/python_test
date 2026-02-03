import pandas as pd
import requests

URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
HEADERS = {"User-Agent": "Mozilla/5.0"}  # Mimic normal browser

def fetch_html(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()  # Raises HTTPError if not 200
    return response.text

def fetch_and_parse_table(url):
    html = fetch_html(url)
    tables = pd.read_html(html)
    return tables[0]

def save_structured_output(df, filename="country_population.csv"):
    df.to_csv(filename, index=False)
    print(f"Saved to {filename}")

def main():
    df = fetch_and_parse_table(URL)
    print(df.head(10))  # Show a quick preview
    save_structured_output(df)

if __name__ == "__main__":
    main()