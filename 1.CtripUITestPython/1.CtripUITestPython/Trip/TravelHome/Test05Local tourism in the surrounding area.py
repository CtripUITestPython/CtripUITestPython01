'''
Ethan
Local tourism in the surrounding area
1. Open the homepage of the Ctrip website
2. Click the "Travel" button on the navigation bar to enter
3.Select the "Beijing" and "Hulunbuir" tourism tabs, click on the "West Lake Scenic Area", "2nd Day", and "This Weekend" options
4.Click on the "Hangzhou 2nd Night Group Tour" button and check
'''

from playwright.sync_api import Playwright, sync_playwright, expect
import time

def Local_tour(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    # Visit the Ctrip website, open the travel menu, click on "Travel_homepage_button"
    page.goto("https://www.ctrip.com/")
    travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)')
    travel_button.click()
    time.sleep(2)
    Travel_homepage_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(1)')
    Travel_homepage_button.click()
    time.sleep(2)
    #Click on the "Beijing" and "Hulunbuir" tourism tabs
    page.locator("[id=\"vac-103045-recommend-tab-境内旅游-北京-2\"]").get_by_text("北京").click()
   
    with page.expect_popup() as page2_info:
        page.locator("[id=\"vac-103045-recommend-banner-境内旅游-2\"]").click()
    page2 = page2_info.value 
    time.sleep(5)
    #Click on the "West Lake Scenic Area", "2nd Day", and "This Weekend" options
    page2.get_by_text("西湖风景名胜区").click()
    page2.get_by_text("2日", exact=True).click()
    page2.get_by_text("本周末").click()
    with page2.expect_popup() as page6_info:
        page2.get_by_text("杭州2日1晚跟团游", exact=True).first.click()
    page6 = page6_info.value
    
    #Check if the button exists, if so, click
    heading_button = page6.get_by_role("heading", name="杭州2日1晚跟团游")
    if heading_button:
        heading_button.click()
    else:
        print("无法找到指定按钮！")
   
    print('Local tourism in the surrounding area test case successful')
    context.close()
    browser.close()

with sync_playwright() as playwright:
    Local_tour(playwright)
