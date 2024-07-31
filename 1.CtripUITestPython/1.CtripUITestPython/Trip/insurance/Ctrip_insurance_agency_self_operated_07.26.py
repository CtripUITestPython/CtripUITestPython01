# @summary --- Jerry
# 1.Verify the contents of the insurance and Ctrip insurance agent self operated module within the tourism module
# 2.After selecting personal property, click on the recommended products and jump to the login page to log in. After logging in, click on 'Protect Rights' to view relevant content
# 3.Close the personal property recommendation interface, click on domestic travel, select recommended products based on sales from high to low, and browse for special protection

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # Insurance
    Ctrip_insurance_agency_self_operated(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# Ctrip_insurance_agency_self_operated
def Ctrip_insurance_agency_self_operated(context: BrowserContext, page: Page) -> None:
    # Travel -> Insurance
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(13)').click()
    # Ctrip Insurance Agency Self operated -> Domestic tourism -> Sales from high to low
    page.locator('a.ico1:nth-child(1)').click()
    page.wait_for_timeout(2000)
    new_page = context.pages[-1]
    new_page.locator('.left-choose span').filter(has_text='销量从高到低').click()
    page.wait_for_timeout(5000)
    # judge -> Browse special protection
    if new_page.locator('.list-con-item').nth(2) == 0:
       print('Search result is empty!') 
    else:
        new_page.locator('.list-con-item').nth(2).click()
    page.wait_for_timeout(2000)
    new_page.locator('i.close.close-icon').click()
    new_page.locator('.detail_tab_col a').filter(has_text='特殊保障').click()
    page.wait_for_timeout(5000)

with sync_playwright() as playwright:
    run(playwright)