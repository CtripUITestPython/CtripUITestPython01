# @summary --- Jerry
# 1.Verify the recommended content for the current season within the study tour module.
# 2.Browsing the first recommended product of the season.

from playwright.sync_api import Playwright, sync_playwright, expect, Page, BrowserContext
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('https://www.ctrip.com')
    # Seasonal_recommendations
    seasonal_recommendations(context, page)
    print('All operations completed！')
    page.wait_for_timeout(5000)
    context.close()
    browser.close()

# Seasonal_recommendations
def seasonal_recommendations(context: BrowserContext, page: Page) -> None:
    # "Travel" -> "Study tour"
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(11)').click()
    # "Judging recommendation results" -> "Browsing seasonal recommendations"
    if page.locator('.iPic').all() == 0:
       print('The recommendation result is empty!')
    else:
       page.locator('.iPic').all()[0].click()
       print("Successfully browsing seasonal recommendations！")
    page.wait_for_timeout(2000)
    
with sync_playwright() as playwright:
    run(playwright)