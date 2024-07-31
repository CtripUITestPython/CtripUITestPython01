from playwright.sync_api import Playwright, sync_playwright, expect

"""
    Ethan
    Test Case 1: Outbound Tourism
    This test case verifies the navigation and functionality for outbound tourism options on the Ctrip website.
    Steps:
    1. Navigate to the Ctrip homepage.
    2. Open the travel menu and click on "Free Travel".
    3. Search for and click on various international travel options such as Japan, Thailand, and the Maldives.
    4. Click the "High-end Tour" link and verify that a new page opens with the correct URL.
"""
def Outbound_tourism(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    # Visit the Ctrip website, open the travel menu, click on "Free Travel"
    page.goto("https://www.ctrip.com/")
    travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)')
    travel_button.click()
    expect(travel_button).to_be_visible()
    Travel_homepage_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(1)')
    Travel_homepage_button.click()
    page.locator("[id=\"vac-103045-recommend-tab-出境旅游-日本-2\"]").get_by_text("日本").click()
    page.locator("[id=\"vac-103045-recommend-tab-出境旅游-泰国-3\"]").get_by_text("泰国").click()
    page.locator("[id=\"vac-103045-recommend-tab-出境旅游-马尔代夫-10\"]").get_by_text("马尔代夫").click()
    page.wait_for_timeout(2000)
    # # Click the "High-end Tour" link and a new page pops up
    with page.expect_popup() as page1_info:
        high_end_travel_link = page.locator('#vac-103045-recommend-tab-出境旅游-高端游-11')
        expect(high_end_travel_link).to_be_visible()
        high_end_travel_link.click()  
    page1 = page1_info.value
    page1.wait_for_load_state("load")
    # Assert the URL of the new page
    expect(page1).to_have_url("https://vacations.ctrip.com/tangram/hhtravel?ctm_ref=vactang_page_5872")
    print('测试用例1：Outbound_tourism成功')
    context.close()
    browser.close()


"""
    Ethan
    Test Case 2: Domestic Tourism
    This test case verifies the navigation and functionality for domestic tourism options on the Ctrip website.
    Steps:
    1. Navigate to the Ctrip homepage.
    2. Open the travel menu and click on "Free Travel".
    3. Search for and click on various surrounding city options.
    4. Click on the "Local Tour Around" link and verify that a new page opens with the correct URL.
"""
def Domestic_tourism(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    # Visit the Ctrip website, open the travel menu, click on "Free Travel"
    page.goto("https://www.ctrip.com/")
    travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4)')
    travel_button.click()
    expect(travel_button).to_be_visible()
    Travel_homepage_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(4) a.lsn_son_nav_LbhRN:nth-child(1)')
    Travel_homepage_button.click()
    expect(Travel_homepage_button).to_be_visible()
    #Search for surrounding cities
    cities = [
        ("杭州", 2), ("苏州", 3), ("普陀山", 4), ("南京", 5), 
        ("舟山", 6), ("乌镇", 7), ("千岛湖", None), 
        ("无锡", 9), ("台州", 10)
    ]
    for city, index in cities:
        if index is not None:
            city_locator = page.locator(f'[id="vac-103045-recommend-tab-周边当地游-{city}-{index}"]').get_by_text(city)
        else:
            city_locator = page.get_by_text(city, exact=True)
        expect(city_locator).to_be_visible()
        city_locator.click()
    page.wait_for_timeout(2000)
    #Click on the "Local Tour Around" link and a new page will pop up
    with page.expect_popup() as page2_info:
        around_travel_link = page.get_by_role("link", name="周边当地游")
        expect(around_travel_link).to_be_visible()
        around_travel_link.click()
    page2 = page2_info.value
    page2.wait_for_load_state("load")
    #Assert the URL of the new page
    expect(page2).to_have_url('https://vacations.ctrip.com/around?startcity=2')  
    print('测试用例2：Domestic Tourism成功')
    context.close()
    browser.close()
with sync_playwright() as playwright:
    Outbound_tourism(playwright)
    Domestic_tourism(playwright)
    
