# @summary --- Jerry
# Verify high-end games by selecting cities from the recommended results for verification and browsing.

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # high_end_tour
    high_end_tour(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# high_end_tour
def high_end_tour(context: BrowserContext, page: Page) -> None:
    # "Travel" -> "high-end travel" -> "The first recommendation"
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(9)').click()
    page.locator('.cui_search.tl_input_wrap_4wLqk').fill('冰岛')
    page.get_by_title(title="搜索").click()

    print("High end tour successfully browsed！")
    page.wait_for_timeout(2000)

with sync_playwright() as playwright:
    run(playwright)