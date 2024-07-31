'''
ethan
 Test11_Discounted_airfare
1. Open the Ctrip website
2. Navigate to the "Special Offer Ticket" page
3. Filter and view flight information from Ningbo to Pudong, Shanghai

'''

from playwright.sync_api import Playwright, sync_playwright, expect
import time

def Discounted_airfare(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto("https://www.ctrip.com/")
    time.sleep(2)
    
    # Locate and click on 'Ticket' to open the menu and select 'Discounted_airfare' 
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(2)').click()
    page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(2) a.lsn_son_nav_LbhRN:nth-child(2)').click()
   
    # Click on Ningbo for detailed information
    page.get_by_text("宁波更多航班").click()
    with page.expect_popup() as page1_info:
        xpath_selector = '//*[@id="__next"]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/a[1]/span'
        page.locator(xpath_selector).click()
    page1 = page1_info.value
    time.sleep(2)
    
    # Perform other filtering operations on the new page
    page1.get_by_text("航空公司").click()
    page1.get_by_text("东方航空 ¥").click()
    page1.get_by_text("起抵时间").click()
    page1.locator("#filter_group_time__depart").get_by_text("晚上 18~24点 ¥").click()
    page1.get_by_text("机场").click()
    page1.get_by_text("浦东国际机场 ¥").click()
    page1.locator("#filter_item_class_grade").get_by_text("").click()
    page1.get_by_text("经济舱 ¥").click()
    page1.get_by_text("更多").click()
    page1.locator("#filter_item_other i").nth(4).click()
    
    context.close()
    browser.close()
    print('Discounted_airfare successful!')

with sync_playwright() as playwright:
    Discounted_airfare(playwright)
