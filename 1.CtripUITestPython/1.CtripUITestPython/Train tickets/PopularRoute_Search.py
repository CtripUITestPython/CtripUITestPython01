from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep

"""
    Test Case : Domestic train tickets - Search for popular routes.
    This test case is mainly for searching for the popular route in the Domestic train tickets.

    Steps:
    1. Enter the train ticket section from the navigation bar → Domestic train tickets.
    2. Click on all discounted routes and print them out.
    3. Verify that all route searches are successful and end the search.

"""

def domestic_travel(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    #Enter the train ticket section from the navigation bar → Domestic train tickets.
    page.goto("https://www.ctrip.com/")
    travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(3)')
    travel_button.click()
    private_travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(3) a.lsn_son_nav_LbhRN:nth-child(1)')
    private_travel_button.click()
    #Choose the recommended route from the popular routes.
    page.get_by_text("热门火车旅游线路").click()
    page.get_by_text("推荐").nth(2).click()
    with page.expect_popup() as page1_info:
        page.get_by_label("京广高铁").click()
    page1 = page1_info.value
    result1=page1.title()
    #Assert that the recommended routes in the popular routes have been successfully searched and printed.
    assert result1 is not None, "热门路线推荐路线搜索失败"
    print("热门火车旅游线路的推荐路线是："+ result1)
    with page.expect_popup() as page2_info:
        page.get_by_label("京沪高铁").click()
    page2 = page2_info.value
    result2=page2.title()
    print("火车旅游线路的推荐路线有："+ result2)
    #Search for other popular routes   
    with page.expect_popup() as page3_info:
        page.get_by_label("宁杭甬高铁").click()
    page3 = page3_info.value
    result3=page3.title()
    print("火车旅游线路的推荐路线有："+ result3)
    with page.expect_popup() as page4_info:
        page.get_by_label("成渝高铁").click()
    page4 = page4_info.value
    result4=page4.title()
    print("火车旅游线路的推荐路线有："+ result4)   
    print("优惠路线搜索完成！")



    context.close()
    browser.close()


with sync_playwright() as playwright:
    domestic_travel(playwright) 