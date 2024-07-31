'''
ethan
1.Open the Ctrip website.
2.Clicks on the "destination" button on the homepage.
3.Enter destination name 'Sichuan' to search for
'''
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def destination(playwright: Playwright) -> None:
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
    
    time.sleep(4)
    page.get_by_text("境外", exact=True).click()
    page.get_by_text("热门", exact=True).click()
    time.sleep(2)
    page.get_by_placeholder("请输入目的地名称").click()
    page.get_by_placeholder("请输入目的地名称").fill("四川")
    page.get_by_placeholder("请输入目的地名称").press("Enter")
    page.locator("#mkt_act_dst_search_btn").click()  
    context.close()
    browser.close()
    print(' destination successful!')

with sync_playwright() as playwright:
    destination(playwright)
