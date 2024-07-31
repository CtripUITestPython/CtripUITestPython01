# @summary --- Jerry
# 1.Verify the content of the personal property module.
# 2.Select personal property, click on the first recommended product, navigate to the page, log in and preview 'Protect Rights' before closing. 

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # Personal_property
    Personal_property(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# Personal_property
def Personal_property(context: BrowserContext, page: Page) -> None:
    # Travel -> Insurance
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(13)').click()
    # Personal property -> Recommendations
    page.locator('.left-tab div').filter(has_text='个人财产').click()
    page.locator('div.intro-con').nth(3).click()
    page.wait_for_timeout(5000)
    new_page = context.pages[-1]
    # Login
    new_page.locator('.form_wrap:nth-child(2) .bbz-js-iconable-input[data-testid="accountNameInput"]').fill('19865043369')
    new_page.locator('.form_wrap:nth-child(2) .bbz-js-iconable-input[data-testid="passwordInput"]').fill('Znb000105@')
    new_page.locator('div[data-testid="checkboxAgreement"]').click()
    new_page.locator('.form_wrap:nth-child(2) .input[data-testid=loginButton]').click()
    print("Login successful!")
    new_page.wait_for_timeout(5000)
    # Browse for protection of rights and interests -> Close
    new_page.locator('i.close.close-icon').click()
    new_page.locator('detail_tab_col li').filter(has_text='保障权益').click()
    page.wait_for_timeout(5000)
    context.pages[-1].close()
    
with sync_playwright() as playwright:
    run(playwright)