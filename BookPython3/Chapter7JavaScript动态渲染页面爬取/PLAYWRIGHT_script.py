from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.locator("#kw").click()
    page.locator("#kw").press("CapsLock")
    page.locator("#kw").fill("NBA")
    page.locator("#kw").press("Enter")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
