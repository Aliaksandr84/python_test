def generate_report(report_dict):
    lines = [f"{col}: {cnt} null values" for col, cnt in report_dict.items()]
    return "\n".join(lines)