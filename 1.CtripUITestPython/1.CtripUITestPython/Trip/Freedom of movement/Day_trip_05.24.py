# @summary --- Jerry
# 1.Verify the theme of Day trip.
# 2.Verify popular recommendations for Day trip and browse them.

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # Day_trip
    Day_trip(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# Day_trip
def Day_trip(context: BrowserContext, page: Page) -> None:
    # "Travel" -> "One day tour" -> "Priority given to positive reviews" -> "The first recommendation"
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(6)').click()
    page.locator('.m_sort_li.active').click()
    page.locator('.m_productcard_container').nth(0).click()
    print("Day trip destination search successful!")
    # Pause for a while and then return to the previous page
    page.wait_for_timeout(2000)

with sync_playwright() as playwright:
    run(playwright)