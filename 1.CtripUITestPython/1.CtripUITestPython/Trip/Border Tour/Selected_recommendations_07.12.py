# @summary --- Jerry
# 1.Validate the content of the selected recommendation module
# 2.Select the departure city, number of days, features, click on the first recommended content preview, and then close it.

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # Selected_recommendations
    Selected_recommendations(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# Selected_recommendations
def Selected_recommendations(context: BrowserContext, page: Page) -> None:
    # "Travel"->"Travel Around" -> "recommendation"
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(8)').click()
    page.locator('.diy_product_img_box:nth-child(2)').click()
    # "Featured Experience" -> "3 days"  -> "Priority given to positive reviews" ->"recommendation"-> "Preview" -> "Close"
    page.locator('.list_cate_select.basefix.list_cate_height:nth-child(3)').filter(has_text='九溪烟树').click()
    page.locator('.list_cate_select.basefix.list_cate_height:nth-child(3)').filter(has_text='3日').click()
    page.locator('.list_recommend_text :nth-child(4)').filter(has_text='3日').click()
    page.locator('.list_product_box.js_product_item:nth-child(1)').click()
    page.wait_for_timeout(2000)
    
with sync_playwright() as playwright:
    run(playwright)