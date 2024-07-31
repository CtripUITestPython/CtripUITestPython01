from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep


"""
    Test Case 5: Outbound private groups
    This test case is mainly for searching for the top rated outbound private group.
    Steps:
    1. Navigate to the Ctrip homepage.
    2. Open the travel menu and click on "Private group".
    3. Select some filter options such as departure city and product type;search for the top rated outbound private group.
    4. Verify that the selected project is a private group,print out the top rated private group.
"""

def domestic_travel(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,args=['--window-size=1600,900'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    # Navigate to the Ctrip homepage, and click on "Private group".
    page.goto("https://www.ctrip.com/")
    travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(3)')
    travel_button.click()
    private_travel_button = page.locator('div.lsn_nav_content_wrap_ci7QT div.lsn_first_nav_wrap_LZamG:nth-child(3) a.lsn_son_nav_LbhRN:nth-child(1)')
    private_travel_button.click()
    #Open the travel menu and click on "Private group".
    page.get_by_role("heading", name="优惠酒店").click()
    page.get_by_text("上海", exact=True).first.click()
    with page.expect_popup() as page1_info:
        page.get_by_text("推荐").nth(1).click()
    page1 = page1_info.value
    sleep(10)

    result=page1.title()
    assert "酒店" in result,"优惠酒店搜索失败,请再试一次"
    print("优惠酒店搜索推荐的是：" + result )
    page1.get_by_placeholder("搜索任何旅游相关").fill("上海地铁")
    with page1.expect_popup() as page2_info:
        page1.get_by_role("link", name="上海地铁音乐文化长廊 上海").click()
    page2 = page2_info.value
    result2=page2.title()
    assert "上海地铁" in result2, "有关上海地铁的搜索失败"
    print("有关上海地铁的搜索是：" + result2)
    page2.get_by_placeholder("搜索任何旅游相关").fill("暑假")
    with page2.expect_popup() as page3_info:
        page2.get_by_text("承德避暑山庄蒙古包度假村").click()
    page3 = page3_info.value
    result3=page.title()
    assert result3 is not None, "暑假相关的搜索失败了"
    print("暑假的相关推荐是：" + result3)
    page3 = page3_info.value
    page3.get_by_placeholder("搜索任何旅游相关").fill("书店")
    with page3.expect_popup() as page4_info:
        page3.get_by_role("link", name="工业园区金鸡湖东/诚品书店 苏州").click()
    page4 = page4_info.value
    result4=page4.title()
    assert result4 is not None, "书店相关搜索失败了"
    print("书店相关的搜索是：" + result4)
    page4.get_by_placeholder("搜索城市/景点/游记/问答/住宿").fill("推荐购买的书")
    page4.get_by_text("搜 索").click()
    with page4.expect_popup() as page5_info:
        page4.get_by_role("img").first.click()
    page5 = page5_info.value
    result5 =page5.title()
    assert result5 is not None, "推荐的书籍搜索失败"
    print("推荐书籍的搜索是：" + result5)
    print("优惠酒店的及旅游线路搜索结束")



    context.close()
    browser.close()


with sync_playwright() as playwright:
    domestic_travel(playwright) 