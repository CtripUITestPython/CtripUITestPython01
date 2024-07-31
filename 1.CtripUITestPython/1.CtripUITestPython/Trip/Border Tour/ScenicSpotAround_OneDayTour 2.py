# @summary --- Jinyu Sun

# 1.Visit scenic spots around
    # Open XieCheng web
    # Switch to the tour around module
    # Varity that the tested area about "visit scenic spots around" exists
    # Click on recommended items --> Varify that you can be redirected to the corresponding web page
    # Click More options, then varity the jumped page exist
# 2.One-day tour around
    # Open XieCheng web
    # Switch to the tour around module
    # Varity that the tested area about "One-day tour around" exists
    # Click on recommended items --> Varify that you can be redirected to the corresponding web page
    # Click on More Options --> Varify that you can be redirected to the corresponding web page 

from playwright.sync_api import Playwright, sync_playwright, expect

class TourAround:
    def __init__(self, playwright: Playwright, headless: bool = False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()

    # Open the tested web
    def navigate_to_page(self):
        self.page = self.context.new_page()
        self.page.goto("https://vacations.ctrip.com/")
        self.page.wait_for_load_state("networkidle")

    # Switch to the tested module
    def click_module(self, module):
        self.page.locator(".pc_home-tabbtnIcon").click()
        self.page.get_by_role("link", name=module, exact=True).click()
        self.page.wait_for_load_state("networkidle")

    # Varity name of the current area
    def varity_area_name(self, areaName):
        area = self.page.get_by_role("heading",name = areaName)
        assert area is not None, "验证失败"
        print(f"验证成功：{areaName}存在")

    # Select a tour and verify that it is accessible
    def select_tour_and_verify(self, xpath, heading_name):
        self.page.locator("body").press("End")
        self.page.wait_for_load_state("networkidle")
        with self.page.expect_popup() as page1_info:
            self.page.locator(xpath).first.click()
        page1 = page1_info.value
        assert page1.get_by_role("heading", name=heading_name) is not None, "验证失败"
        print("成功访问")

    # Varity more option module
    def more_options1(self, xpath, titleName):
        with self.page.expect_popup() as page2_info:
            self.page.locator(xpath).click()
        page2 = page2_info.value
        page2.wait_for_load_state("networkidle")
        title = page2.title()
        assert titleName in title, "跳转失败"
        print("跳转成功")

    def more_options2(self, xpath, selectedItem):
        with self.page.expect_popup() as page1_info:
            self.page.locator(xpath).click()
        page1 = page1_info.value
        with page1.expect_popup() as page2_info:
            page1.get_by_role("link", name=selectedItem).click()
        page2 = page2_info.value
        page2.wait_for_load_state("networkidle")
        assert page2.get_by_role("heading", name=selectedItem) is not None, "跳转失败"
        print("跳转成功")

    # close all webs
    def close(self):
        self.context.close()
        self.browser.close()


# Visit scenic spots around
with sync_playwright() as playwright:

    print("周边逛景点测试结果")
    VisitSpotsAround = TourAround(playwright)
    VisitSpotsAround.navigate_to_page()
    VisitSpotsAround.click_module("周边游")
    VisitSpotsAround.varity_area_name("周边逛景点")
    VisitSpotsAround.select_tour_and_verify("div:nth-child(8) > .expose_dom > .diy_product_wrapper > .diy_product_pc_box > .diy_product_box > .diy_product_content > .diy_card_content_list > div > div:nth-child(3) > .diy_product_img_box > .diy_product_img","陆家嘴")
    VisitSpotsAround.close()

    print("查看更多测试结果：")
    VisitSpotsAround = TourAround(playwright)
    VisitSpotsAround.navigate_to_page()
    VisitSpotsAround.click_module("周边游")
    VisitSpotsAround.varity_area_name("周边逛景点")
    VisitSpotsAround.more_options1("div:nth-child(7) > .hot_zone_box > .hot_zone_content > .hot_zone_wrapper > .hot_zone_item","自由行攻略指南")
    VisitSpotsAround.close()

# One-day tour around
with sync_playwright() as playwright:
    print("周边一日游测试")
    OneDayTour = TourAround(playwright)
    OneDayTour.navigate_to_page()
    OneDayTour.click_module("周边游")
    OneDayTour.varity_area_name("周边一日游")
    OneDayTour.select_tour_and_verify("div:nth-child(2) > .expose_dom > .diy_product_wrapper > .diy_product_pc_box > .diy_product_box > .diy_product_content > .diy_card_content_list > div > div > .diy_product_img_box > .diy_product_img","丽水3日2晚跟团游")
    OneDayTour.close()

    print("查看更多测试结果：")
    OneDayTour = TourAround(playwright)
    OneDayTour.navigate_to_page()
    OneDayTour.click_module("周边游")
    OneDayTour.varity_area_name("周边一日游")
    OneDayTour.more_options2("div:nth-child(4) > .hot_zone_box > .hot_zone_content > .hot_zone_wrapper > .hot_zone_item","嘉兴乌镇一日游【好评1")
    OneDayTour.close()