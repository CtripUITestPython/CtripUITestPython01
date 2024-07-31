from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep

"""
    Oliver
    Test Case 4: Destination private groups
    This test case mainly verifies that the city search function of the private group is normal on the Ctrip website.
    Steps:
    1. Navigate to the Ctrip homepage.
    2. Open the travel menu and click on "Private group".
    3. Select some filter options such as departure city and product type;Choose positive feedback first.
    4. Verify that the selected project is a private group,print out the top rated private group.
"""


def domestic_travel(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    # Navigate to the Ctrip homepage, and click on "Private group".
    page.goto("https://www.ctrip.com/")
    travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)')
    travel_button.click()
    private_travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(3)')
    private_travel_button.click()
    #Open the travel menu and click on "Private group".
    page.get_by_role("link", name="私家团", exact=True).click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="目的地私家团").click()
    page1 = page1_info.value
    page1.get_by_role("link", name="搜 索").click()
    page1.locator("#filter_box_point").get_by_text("上海").click()
    page1.locator("#filter_box_point").get_by_text("私家团").click()
    page1.get_by_text("好评优先").click()
    #Verify that the selected project is a private group,print out the top rated private group.
    with page1.expect_popup() as page2_info:
        page1.get_by_role("img").first.click()
    page2 = page2_info.value
    sleep(10)
    result=page2.title()
    print(result)
    assert "私家团" in result,"目的地私家团搜索团失败"
    print("上海出发目的地私家团推荐" + result )
            
    context.close()
    browser.close()


with sync_playwright() as playwright:
    domestic_travel(playwright) 