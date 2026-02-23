from playwright.sync_api import sync_playwright
import os
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        # Determine absolute path to index.html
        cwd = os.getcwd()
        file_url = f"file://{cwd}/index.html"

        print(f"Navigating to: {file_url}")
        page.goto(file_url)

        # Wait for the loader to disappear (animation takes ~2s total)
        print("Waiting for loader animation...")
        time.sleep(2.5)

        # Scroll to trigger AOS animations
        print("Scrolling to trigger animations...")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1) # Wait for animations
        page.evaluate("window.scrollTo(0, 0)")
        time.sleep(1)

        # Take full page screenshot
        screenshot_path = "verification/redesign_screenshot.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to: {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()
