# data_quality/playwright_agent.py

from playwright.sync_api import sync_playwright

def fetch_html_playwright(url):
    """
    Uses Playwright to fetch HTML content of a web page.
    Returns the raw HTML string.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        # Optionally wait for a selector or some dynamic content to load
        # page.wait_for_selector("table")  
        html = page.content()
        browser.close()
        return html

# Example usage
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    html = fetch_html_playwright(url)
    # Save HTML to file or parse with pandas
    with open("page.html", "w", encoding="utf-8") as file:
        file.write(html)
    print("HTML saved to page.html")