# @summary --- Jerry
# 1. Verify all content related to cruise travel
# 2. Verify by locating, clicking on search, and selecting departure city, cruise route, cruise brand, and cruise name to select the recommended first product
# 3. Verify the travel calendar, select the recommended first item by selecting the departure time and cruise route, and click to enter the details interface to view the cost description

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # Tourism_Cruise
    Cruise(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# Tourism_Cruise  
def Cruise(context: BrowserContext, page: Page) -> None:
    # "Travel" -> "Cruise" -> "Search" 
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(5)').click()
    page.locator('.s_btn').click()
    # "More" -> "Shanghai" -> "More"
    page.locator('.flt_item:nth-child(1) .more').click()
    page.locator('.flt_item:nth-child(1) .items_inner a').filter(has_text='上海').click()
    page.locator('.flt_item:nth-child(1) .more').click()
    # "Antarctica" -> "Heidelberg Cruise" -> "Nansen"
    page.locator('.flt_item:nth-child(1) .items_inner a').filter(has_text='南极').click()
    #  "judge" -> "First Product" -> "Close"
    if page.locator('.route_title').nth(0) == 0:
       print('Search result is empty!') 
       return()   
    else:
        page.locator('.route_title').nth(0).click()
    page.wait_for_timeout(2000)
    context.pages[-1].close()
    page.locator('.clear').click()

    # "Travel time - More" -> "December" ->"Cruise routes - More" -> "Arctic" -> "First product" 
    page.locator('.flt_item:nth-child(3) .more').click()
    page.locator('.flt_item:nth-child(3) .items_inner a').filter(has_text='12月').nth(0).click()
    page.locator('.flt_item:nth-child(2) .more').click()
    page.locator('.flt_item:nth-child(2) .items_inner a').filter(has_text='北极').nth(0).click()
    page.wait_for_timeout(2000)

with sync_playwright() as playwright:
    run(playwright)