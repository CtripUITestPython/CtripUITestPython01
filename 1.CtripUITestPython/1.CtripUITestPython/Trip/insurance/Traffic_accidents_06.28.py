# @summary --- Jerry
# 1.Verify the content of the traffic accident module
# 2.Select the first recommended content and log in, preview, and finally close.

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # Traffic_accidents
    traffic_accidents(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

#   Traffic_accidents
def traffic_accidents(context: BrowserContext, page: Page) -> None:
    # "Travel" -> "Insurance" -> "Unexpected health" -> "recommendation"
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(13)').click()
    page.locator('div.index_filter.index-filter-new div.left-tab:nth-child(2) div.tab-item.current').click()
    page.locator('div.pro-tit.line2:nth-child(2)').click()
    # "Login"  -> "Special protection"-> "Preview" -> "Close"
    page.locator('.form_wrap:nth-child(2) .bbz-js-iconable-input[data-testid="accountNameInput"]').fill('19865843369')
    page.locator('.form_wrap:nth-child(2) .bbz-js-iconable-input[data-testid="passwordInput"]').fill('Znb000105@')
    page.locator('div[data-testid="checkboxAgreement"]').click()
    page.locator('.form_wrap:nth-child(2) input[data-testid=loginButton]').click()
    print("Login successful and preview！")
    page.locator('div.sure-btn:nth-child(2)').click()
    page.get_by_role('link',name="保障权益").click()
    page.wait_for_timeout(5000)
    
with sync_playwright() as playwright:
    run(playwright)