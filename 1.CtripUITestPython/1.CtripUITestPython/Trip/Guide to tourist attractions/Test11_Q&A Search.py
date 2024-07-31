from playwright.sync_api import Playwright, sync_playwright, TimeoutError as PlaywrightTimeoutError
import time

# Ethan
# Test10_QA_Search
# This script automates the process of searching for scenic spots in Shanghai on the Ctrip website. 
# It navigates through multiple pages to find and select specific scenic spots.

def QA_Search(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    
    try:
        # Navigate to Ctrip website
        page.goto("https://www.ctrip.com/", timeout=60000)
        time.sleep(4)
        
        # Click on the "Explore Scenic Spots" button
        Explore_Scenic_Spots_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(5)')
        Explore_Scenic_Spots_button.click()
        time.sleep(2)
        
        # Fill in the search input with "上海"
        page.get_by_placeholder("搜索城市/景点/游记/问答/住宿").fill("上海")
        time.sleep(2)
        
        # Click on the search result for "上海, 中国" and handle the popup
        with page.expect_popup() as page1_info:
            page.get_by_role("link", name="上海, 中国").click()
        page1 = page1_info.value
        time.sleep(2)
        
        # Click on the "景点" link in the new page and handle the popup
        with page1.expect_popup() as page2_info:
            page1.get_by_text("景点", exact=True).click()
        page2 = page2_info.value
        time.sleep(2)
        
        # Apply filters for 2km, "亲子同乐", and "好评优先"
        page2.get_by_text("2km").click()
        page2.get_by_text("亲子同乐").click()
        page2.get_by_text("好评优先").click()
        time.sleep(2)
        
        # Click on the "南京路步行街" link and handle the popup
        with page2.expect_popup() as page3_info:
            page2.get_by_role("link", name="南京路步行街").click()
        page3 = page3_info.value
        time.sleep(2)
        
        # Assertion to verify the page title
        assert page3.title() == "上海南京路步行街游玩攻略简介,上海南京路步行街门票/地址/图片/开放时间/照片/门票价格【携程攻略】", "Failed to navigate to the expected destination page"

        print('QA_Search completed successfully!')
        
    except PlaywrightTimeoutError:
        print("The page took too long to load and timed out.")
        
    finally:
        # Ensure the context and browser are closed
        context.close()
        browser.close()

with sync_playwright() as playwright:
    QA_Search(playwright)
