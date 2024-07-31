'''
Cruise_ships
Ethan
1. Open the homepage of the Ctrip website
2. Click the "Travel" button on the navigation bar to enter
3. Enter the cruise ship name in the search box and select search
4. Choose routes departing from Shanghai and July
5. Click on the first cruise product to enter the details page

'''

from playwright.sync_api import Playwright, sync_playwright
import time

def Cruise_ships(playwright: Playwright) -> None:
    browser = None
    try:
        #Start the Chromium browser and set the window size to open the Ctrip website homepage
        browser = playwright.chromium.launch(headless=False, args=['--window-size=1600,900'])
        context = browser.new_context(viewport={'width': 1600, 'height': 900})
        page = context.new_page()
        page.goto("https://www.ctrip.com/")
        
        #Locate and click on the "Travel" button in the navigation bar to ensure that the "Travel" button is visible
        travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)')
        travel_button.click()
        if travel_button.is_visible():
            Travel_homepage_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(5)')
            Travel_homepage_button.click()
            
            #Enter the name of the cruise ship in the search box and click to check if there is a result for the 'Aida Magic City'
            page.get_by_placeholder("搜索邮轮、航线或目的地").click()
            cruise_result = page.get_by_text("爱达魔都号")
            if cruise_result.count() > 0:
                print("成功找到爱达魔都号")
                cruise_result.click()
                
                #Choose the cruise route departing from Shanghai, choose the cruise route for July, and click on the first cruise product
                page.get_by_test_id("filter_s").get_by_role("link", name="上海").click()
                page.locator("#filterContainer > div > div:nth-child(2) > div.bd > div > a:nth-child(3) > span").click()
                with page.expect_popup() as page1_info:
                    page.locator('//*[@id="ProductContainer"]/div[1]/div[3]/a/div[2]/h2').click()
                    print("Cruise_ships test case successful")
            else:
                print("没有找到爱达魔都号")
        else:
            print("旅行按钮不可见")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if browser:
            browser.close()

with sync_playwright() as playwright:
    Cruise_ships(playwright)
