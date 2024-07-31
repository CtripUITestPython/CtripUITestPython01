# @summary --- Jerry
# 1.Verify the content of the Domestic independent travel module
# 2.Select the departure city, travel days, sales volume, and other related information
# 3.Check if the recommended list is empty, and click on the first recommended product for preview before closing it

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # Domestic_independent_travel
    Domestic_independent_travel(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# Domestic_independent_travel
def Domestic_independent_travel(context: BrowserContext, page: Page) -> None:
    # "Travel"->"independent travel" -> "Surrounding independent travel" -> "More selected products"
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(4)').click()
    page.locator('.more_a:nth-child(2)').click()
    # "Departing from Hangzhou" -> "3 days" -> "Sales priority" 
    page.locator('.list_cate_select.basefix.list_cate_height:nth-child(2)').filter(has_text='杭州').click()
    page.locator('.list_cate_select.basefix.list_cate_height:nth-child(2)').filter(has_text='3日').click()
    page.locator('.list_recommend_text :nth-child(3)').click()
    # "Check if the recommended product list is not empty" -> "recommendation"-> "Preview" -> "Close"
    if len(page.locator('.list_product_box.js_product_item:nth-child(1)').all()) == 0:
        print('Search result is empty!')
    else:
        page.locator('.list_product_box.js_product_item:nth-child(1)').click()
    print("Preview the first recommended product！")
    page.wait_for_timeout(2000)
    
with sync_playwright() as playwright:
    run(playwright)