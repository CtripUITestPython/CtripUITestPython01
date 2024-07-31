'''
ethan
Flight dynamic search
1. Open the Ctrip website
2. Navigate to the "Flight Tickets" page
3. Search for flight number and landing location
'''
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def Flight_dynamic_search(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto("https://www.ctrip.com/")
    time.sleep(2)
    
    # Locate and click on the 'Ticket' button
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(2)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(2) a.lsn_son_nav_LbhRN:nth-child(3)').click()
    time.sleep(2) 
    
    # Search for flight number "MU5099"
    page.get_by_text("搜航班号").click()
    page.get_by_placeholder("请填写航班号，如MU1234").fill("MU5099")
    page.get_by_text("搜索").click()
    time.sleep(2)
    
    # Search for takeoff and landing locations and fill in the departure and arrival cities or airports
    page.get_by_text("搜起降地").click()
    page.get_by_placeholder("请填写出发城市或机场").click()
    page.get_by_text("北京", exact=True).click()
    page.get_by_placeholder("请填写到达城市或机场").click()
    page.get_by_text("中国澳门", exact=True).click()
    page.get_by_text("搜索").click()
    time.sleep(2)

    context.close()
    browser.close()
    print('Flight_dynamic_search successful!')

with sync_playwright() as playwright:
    Flight_dynamic_search(playwright)
