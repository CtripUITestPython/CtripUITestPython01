'''
Ethan
Test07_Travel_Notes_Search
1.Open the Ctrip website.
2.Clicks on the "Explore Scenic Spots" button on the homepage.
3.Enters "上海" (Shanghai) into the search input field and presses Enter.
4.Expects and interacts with a popup, clicking on a link that contains the text "外滩, 上海The Bund4.8分999+条评论" 
5.Checks that the URL of the opened page matches 'https://you.ctrip.com/sight/shanghai2/736.html'.
'''
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def Travel_Notes_Search(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    # Navigate to Ctrip website,Click on the "Explore Scenic Spots" button
    page.goto("https://www.ctrip.com/")
    Explore_Scenic_Spots_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(5)')
    Explore_Scenic_Spots_button.click()
    # Fill in the search input with "上海" and press Enter
    page.get_by_placeholder("搜索城市/景点/游记/问答/住宿").fill("上海")
    time.sleep(2)
    page.get_by_placeholder("搜索城市/景点/游记/问答/住宿").press("Enter")
    # Expect a popup and click on a specific link containing "外滩, 上海The Bund4.8分999+条评论"
    with page.expect_popup() as page1_info:
    
      page.locator("a").filter(has_text="外滩, 上海The Bund4.8分999+条评论").click()
    
    page1 = page1_info.value
    time.sleep(2)
    # Expect the URL of the new page to be 'https://you.ctrip.com/sight/shanghai2/736.html'
    expect(page1).to_have_url('https://you.ctrip.com/sight/shanghai2/736.html')
    print('Test07-Travel-Notes-Search successful!')
    context.close()
    browser.close()

with sync_playwright() as playwright:
    Travel_Notes_Search(playwright)
