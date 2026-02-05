import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.nba.com/")
    page.get_by_role("link", name="Games", exact=True).click()
    page.get_by_role("button", name="I Accept").click()
    page.get_by_role("link", name="Box score").first.click()
    page.get_by_role("button", name="close email sign up banner").click()
    page.get_by_text("Joel Embiid").scroll_into_view_if_needed()
    # page.get_by_role("link", name="Joel Embiid").click()
    page.get_by_role("tablist").get_by_role("link", name="Stats").click()
    page.get_by_role("button", name="close download dialog").click()

    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
