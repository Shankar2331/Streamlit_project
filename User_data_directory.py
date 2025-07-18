from playwright.async_api import async_playwright
import asyncio
import os

USER_DATA_DIR = os.path.join(os.getcwd(), "user-data")

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            USER_DATA_DIR,
            headless=False,
            args=[
                "--start-maximized",
                # optional flags to look more “real”
                "--disable-blink-features=AutomationControlled",
            ],
        )
        page = await browser.new_page()
        await page.goto("https://mail.google.com/")
        # If you’re already signed in, you’ll land in the inbox.
        # Otherwise, sign in by hand, and the cookies get saved automatically.
        await page.wait_for_timeout(70000)  # give yourself 30s to login once
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())