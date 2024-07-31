'''
Ethan
Test06_Local entertainment
1. Open the Ctrip website.
2. Click to enter the travel section and further navigate to the travel homepage.
3. On the local entertainment recommendations page, click on multiple cities.
4. Perform filtering and clicking actions on the popup page that appears.
5. Finally, verify that the title of the second popup page contains the specific text "东方明珠".

'''

from playwright.sync_api import Playwright, sync_playwright, expect
import time
import re

def Local_entertainment(playwright: Playwright) -> None:
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
    #Click on Chengdu, Xiamen, and Lijiang in sequence on the local entertainment recommendation page
    page.locator("[id=\"vac-103045-recommend-tab-当地玩乐-成都-2\"]").get_by_text("成都").click()
    page.locator("[id=\"vac-103045-recommend-tab-当地玩乐-厦门-3\"]").get_by_text("厦门").click()
    page.locator("[id=\"vac-103045-recommend-tab-当地玩乐-丽江-4\"]").get_by_text("丽江").click()
    time.sleep(2)
    #Wait for a new pop-up window to open and retrieve its page instance
    with page.expect_popup() as page1_info:
       page.locator("[id=\"vac-103045-recommend-banner-当地玩乐-1\"]").click()
    page1 = page1_info.value
    time.sleep(2)
    #Filter in the first pop-up page
    page1.locator("[id=\"act-10650047360-filter-select-2-1daytrip-线路-72-fxb2_381\"] i").click()
    page1.locator("[id=\"act-10650047360-filter-select-2-1daytrip-景点\\/场馆-67-75611\"] i").click()
    page1.locator("[id=\"act-10650047360-filter-select-2-1daytrip-出发城市-65-2\"] i").click()
    time.sleep(2)
    #Wait for the second pop-up page to open and retrieve its page instance
    with page1.expect_popup() as page2_info:
        page1.get_by_role("link", name="上海东方明珠+浦江游览+城隍庙旅游区+外滩一日游【特牌+优选精品团+夜游船/杜莎蜡像馆/观光隧道/上博等可选】").click()
    page2 = page2_info.value
    time.sleep(2)
    #Get the title of the second pop-up page and check whether it contains "Oriental Pearl TV Tower"
    page2_title = page2.title()
    assert re.search("东方明珠", page2_title), f"页面标题 '{page2_title}' 不包含 '东方明珠'"
    
    context.close()
    browser.close()
    print('Local_entertainment successful!')

with sync_playwright() as playwright:
    Local_entertainment(playwright)