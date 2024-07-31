# @summary --- Jerry
# 1.Verify the theme of free travel.
# 2.Verify by searching for cities in the search box again.
# 3.Verify popular recommendations for search cities and browse them.

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # city_search
    city_search(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# city_search
def city_search(context: BrowserContext, page: Page) -> None:
    # "Travel" -> "Free Travel" -> "Free Travel Search Box" -> "Free Travel Search Button"
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(4)').click()
    page.locator('.search_txt').fill('哈尔滨')
    page.locator('.main_search_btn').click()
    page.locator('.list_product_item.flex.flex-row').nth(0).click()
    print("City search successful！")
    # Pause for a while and then return to the previous page
    page.wait_for_timeout(2000)

with sync_playwright() as playwright:
    run(playwright)