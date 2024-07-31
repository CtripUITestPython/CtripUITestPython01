# @summary --- Jinyu Sun

# 1.Varity travel notes
    # Open XieCheng web
    # Switch to the study tour module
    # Varity that the tested area about "travel notes" exists
    # Click on recommended items --> Verify that you can be redirected to the corresponding web page
# 2.Varity tour around
    # Open XieCheng web
    # Switch to the tour around
    # Varity that the tested area about "tour around" exists
    # Click on recommended items --> Verify that you can be redirected to the corresponding web page
    # Click on More Options --> Verify that you can be redirected to the corresponding web page 

from playwright.sync_api import Playwright, sync_playwright, expect

class StudyTour:
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
    def more_options(self, xpath):
        with self.page.expect_popup() as page2_info:
            self.page.locator(xpath).click()
        page2 = page2_info.value
        page2.wait_for_load_state("networkidle")
        title = page2.title()
        assert "自由行攻略指南" in title, "跳转失败"
        print("跳转成功")

    def travel_notes(self):
        self.page.locator(".next").click()
        self.page.locator(".prev").click()
        with self.page.expect_popup() as page1_info:
            self.page.get_by_role("link", name="那片星空那片海，那群伙伴那座城，想念在土澳的共同时光 携程游学发表于 2018-09-").first.click()
        page1 = page1_info.value
        page1.wait_for_load_state("networkidle")
        title = page1.title()
        assert "旅游" in title, "跳转失败"
        print("跳转成功")

    # close all webs
    def close(self):
        self.context.close()
        self.browser.close()



# Travel notes
with sync_playwright() as playwright:
    TravelNote = StudyTour(playwright)
    print("精选游记测试结果")
    TravelNote.navigate_to_page()
    TravelNote.click_module("游学")
    TravelNote.varity_area_name("精选游记")
    TravelNote.travel_notes()
    TravelNote.close()

#  Tour around
with sync_playwright() as playwright:

    print("周边逛景点测试结果")
    TourAround = StudyTour(playwright)
    TourAround.navigate_to_page()
    TourAround.click_module("周边游")
    TourAround.varity_area_name("周边逛景点")
    TourAround.select_tour_and_verify("div:nth-child(8) > .expose_dom > .diy_product_wrapper > .diy_product_pc_box > .diy_product_box > .diy_product_content > .diy_card_content_list > div > div:nth-child(3) > .diy_product_img_box > .diy_product_img","陆家嘴")
    TourAround.close()

    print("查看更多测试结果：")
    TourAround = StudyTour(playwright)
    TourAround.navigate_to_page()
    TourAround.click_module("周边游")
    TourAround.varity_area_name("周边逛景点")
    TourAround.more_options("div:nth-child(7) > .hot_zone_box > .hot_zone_content > .hot_zone_wrapper > .hot_zone_item")
    TourAround.close()