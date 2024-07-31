# @summary --- Jerry
# Verify the theme game by searching in the search box and clicking to browse the first recommended product.

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # theme_tour
    theme_tour(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# theme_tour
def theme_tour(context: BrowserContext, page: Page) -> None:
    # "Travel" -> "Theme_tour" -> "Search box filled 户外" -> "新疆北疆"
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(10)').click()
    page.locator('.search_input').fill('户外')
    page.locator('.theme_search_btn').click()
    if page.locator('.route_title').all() == 0:
       print('Search result is empty!')
    else:
        page.get_by_role("image", name="新疆北疆+乌鲁木齐+喀纳斯+赛里木湖8日7晚拼小团").click()
    print("Theme tour successfully browsed！")
    page.wait_for_timeout(2000) 
    
with sync_playwright() as playwright:
    run(playwright)