from playwright.sync_api import sync_playwright
import os
import time

# Set URL and output paths
URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
CHAPTER_FILE = "chapter.txt"
SCREENSHOT_FILE = "chapter.png"

def scrape_chapter():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            print(f"Navigating to: {URL}")
            page.goto(URL)

            time.sleep(2)  # let content load

            print("Taking screenshot...")
            page.screenshot(path=SCREENSHOT_FILE, full_page=True)

            print("Extracting text...")
            content = page.inner_text("#mw-content-text")

            print(f"Saving content to {CHAPTER_FILE}...")
            with open(CHAPTER_FILE, "w", encoding="utf-8") as f:
                f.write(content)

            browser.close()
            print("✅ Scraping completed successfully.")

    except Exception as e:
        print(f"❌ Error during scraping: {e}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"📁 Current directory: {current_dir}")
    scrape_chapter()
