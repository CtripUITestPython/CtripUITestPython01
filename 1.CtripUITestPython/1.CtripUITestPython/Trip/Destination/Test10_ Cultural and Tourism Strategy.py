'''
ethan
Test10_ Cultural and Tourism Strategy
1.Open the Ctrip website.
2.Clicks on the "destination" button on the homepage.
3.Navigation to specific tourist destination pages
'''
from playwright.sync_api import Playwright, sync_playwright, TimeoutError as PlaywrightTimeoutError
import time

def destination(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    
    try:
        page.goto("https://www.ctrip.com/", timeout=60000)  # Increased timeout to 60 seconds
        time.sleep(4)
        
        # Locate and click the 'Travel' button
        travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)')
        travel_button.click()
        time.sleep(2)
        
        # Locate and click the 'destination' button
        destination_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(15)')
        destination_button.click()
        time.sleep(4)
         # Handle the first popup window,Click on the '推荐' link in the new page
        with page.expect_popup() as page2_info:
            page.get_by_role("link", name="山南，隐世红尘间的西藏 小布行路上 小布行路上").click()
        page2 = page2_info.value
        page2.get_by_role("link", name="推荐").click()
        time.sleep(2)
        # Handle the second popup window
        with page2.expect_popup() as page4_info:
            page2.locator('a.cpt[title="两个人的台北之旅——台北深度游"]').click()
        page4 = page4_info.value
        
        time.sleep(2)
        
        # Assertion to verify successful navigation
        assert page4.title() == "两个人的台北之旅——台北深度游 - 台北游记攻略【携程攻略】", "Failed to navigate to the expected destination page"
        
        print('Cultural and Tourism Strategy successful!')
        
    except PlaywrightTimeoutError:
        print("The page took too long to load and timed out.")
        
    finally:
        context.close()
        browser.close()

with sync_playwright() as playwright:
    destination(playwright)
