'''
ethan
1.Open the Ctrip website.
2.Navigate through the website to explore different travel destinations.
3.Click on specific buttons and links to access detailed information about local entertainment options.
'''
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def View_flagship_store(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto("https://www.ctrip.com/")
    time.sleep(4)
    # Locate and click the 'Travel' button
    travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)')
    
    travel_button.click()
    time.sleep(2)
    
    # Locate and click the 'destination' button
    destination_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(15)')
    destination_button.click()
    time.sleep(2)
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="查看更多旗舰店 >").click()
    page1 = page1_info.value
    time.sleep(2)
    page1.get_by_text("北美洲").click()
    time.sleep(2)
    with page1.expect_popup() as page2_info:
        page1.get_by_role("link", name="加拿大BC省官方旗舰店 狂野自然 尽在我心").click()
    page2 = page2_info.value

    context.close()
    browser.close()
    print('View_flagship_store successful!')

with sync_playwright() as playwright:
    View_flagship_store(playwright)
