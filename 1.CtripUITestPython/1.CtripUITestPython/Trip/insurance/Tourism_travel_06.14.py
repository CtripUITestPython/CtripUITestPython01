# @summary --- Jerry
# 1.Verify the query function within the insurance module.
# 2.After querying, the page will redirect to login and preview.

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # Tourism_travel
    tourism_travel(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# Tourism_travel
def tourism_travel(context: BrowserContext, page: Page) -> None:
    # "Travel" -> "Insurance" -> "Harbin"
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(13)').click()
    page.locator('.inputSel.f_error').fill('哈尔滨')
    page.get_by_role('link',name="快速查询").click()
    # "Login" -> "Preview" -> "Close"
    page.locator('.form_wrap:nth-child(2) .bbz-js-iconable-input[data-testid="accountNameInput"]').fill('19865843369')
    page.locator('.form_wrap:nth-child(2) .bbz-js-iconable-input[data-testid="passwordInput"]').fill('Znb000105@')
    page.locator('div[data-testid="checkboxAgreement"]').click()
    page.locator('.form_wrap:nth-child(2) input[data-testid=loginButton]').click()
    print("Login successful and preview！")
    page.wait_for_timeout(2000)
    
with sync_playwright() as playwright:
    run(playwright)