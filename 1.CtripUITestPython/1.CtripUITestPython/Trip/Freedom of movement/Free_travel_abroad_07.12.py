# @summary --- Jerry
# 1.Verify the content of the domestic free movement module
# 2.Select the departure city, number of days, click on the first recommended content preview and close it.

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # Free_travel_abroad
    Free_travel_abroad(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# Free_travel_abroad
def Free_travel_abroad(context: BrowserContext, page: Page) -> None:
    # "Travel"->"Free Travel" -> "Free travel abroad" -> "上海" -> "3日"  -> "recommendation"-> "Preview" -> "Close"
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(4)').click()
    page.locator('.pro_title dw_inner a.more_a:nth-child(2)').click()
    page.locator('.list_cate_content_basefix:nth-child(1)').filter(has_text='上海').click()
    page.locator('.list_cate_content_basefix:nth-child(2)').filter(has_text='3日').click()
    page.locator('.list_product_title').all()[0].click()
    page.wait_for_timeout(2000)
    context.pages[-1].close()
    
with sync_playwright() as playwright:
    run(playwright)