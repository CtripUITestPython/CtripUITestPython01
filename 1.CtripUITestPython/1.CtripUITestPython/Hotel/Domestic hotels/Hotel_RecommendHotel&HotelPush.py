# @summary --- Jinyu Sun
# Varity the Hotel pivot

# module 1: Varity Hotel recommendation module
    # case 1: varity the recommended hotel on the current page
        # Open XieCheng web
        # Switch to the Hotel pivot
        # Varify that the Hotel recommendation module exists
        # Click on the recommended hotel --> Verify that you can be redirected to the corresponding web page

    # # case 2: varity the recommended regions on the current page
        # Open XieCheng web
        # Switch to the Hotel pivot
        # Varify that the Hotel recommendation module exists
        # Varity that the displayed region number is as expected and output all region name

# module 2: Varity the Hot push in the season module
    # case 1: varity that the tour in the the Hot push in the season & Package tour can be accessed
        # Open XieCheng web
        # Switch to the Hotel pivot
        # Varify that the Hot push in the season module exists
        # Varity that the the Hot push in the season & Package tour exists
        # Click on the recommended tour --> Verify that you can be redirected to the corresponding web page

    # # case 2: varity that the airline ticket in the dscounted airfare module can be acceseed
        # Open XieCheng web
        # Switch to the Hotel pivot
        # Varify that the Hot push in the season module exists
        # Varify that the dscounted airfare module exists
        # Click on the recommended airline ticket --> Verify that you can be redirected to the corresponding web page

from playwright.sync_api import Playwright, sync_playwright, expect

class TourHotel:
    def __init__(self, playwright: Playwright, headless: bool = False):
        self.playwright = playwright
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()

    # Open the tested web
    def navigate_to_page(self):
        self.page = self.context.new_page()
        self.page.goto("https://vacations.ctrip.com/")
        self.page.wait_for_load_state("networkidle")

    # make the current window maximize
    def maximize_window(self):
        self.page.set_viewport_size({"width": 1920, "height": 1080})

    # Switch to the tested module
    def click_module(self, module):
        self.page.locator(".pc_home-tabbtnIcon").click()
        self.page.get_by_label(module).click()
        self.page.wait_for_load_state("networkidle")

    # Varity name of the current area
    def varity_area_name(self, areaName):
        area = self.page.get_by_role("heading",name = areaName)
        assert area is not None, "验证失败"
        print(f"验证成功：{areaName}存在")

    # Varity the selected hotel
    def varity_hotel(self):
        theClickedItemText = self.page.locator('div.pas_hotel-container_D5uyO > ul.pas_hotel_8EyaF > li:nth-child(2) a > div.pas_info_GCPkI h3').text_content()
        self.page.locator('div.pas_hotel-container_D5uyO > ul.pas_hotel_8EyaF > li:nth-child(2) a').click()
        self.page.wait_for_load_state("networkidle")
        jumpedWindow = self.page.get_by_text(f"{theClickedItemText}")
        assert jumpedWindow is not None, "验证失败"
        print(f"成功访问{theClickedItemText}")

    # Varity the displayed area
    def varity_theSelectedAreaNumber(self):

        # Get all the displayed regions
        buttons = self.page.locator('div.pas_container_0P0Vy > div.pas_header_WsFwT.pas_flex-between_Aovg- > ul.pas_ul_EH8fT > button')
        button_count = buttons.count()
        assert button_count == 4, "验证失败"
        print(f"验证成功，所显示的地区模块数量为{button_count}")

        # Output all regions by traversal
        for index in range(button_count):
            button_text = buttons.nth(index).text_content()
            print(f"分别是{button_text}")

    # Varity the selected tour
    def varity_tour(self):
        getText = self.page.locator('div.pas_recommend-container_2uDvk > div.pas_group_I902J > ul.pas_r-ul_ZTteF > li:nth-child(1) a > div.pas_image-container_MqeR6 img').get_attribute('alt')
        self.page.locator('div.pas_recommend-container_2uDvk > div.pas_group_I902J > ul.pas_r-ul_ZTteF > li:nth-child(1) a').click()
        self.page.wait_for_load_state("networkidle")
        jumpedWindowElement = self.page.get_by_text(f"{getText}")
        assert jumpedWindowElement is not None, "验证失败"
        print(f"成功访问{getText}")

    def varity_airlineTicket(self, xpath, jempedKeyword):
        self.page.locator(xpath).click()
        self.page.wait_for_load_state("networkidle")
        NewWindow = self.page.get_by_text(jempedKeyword)
        assert NewWindow is not None, "验证失败"
        print("成功访问特价机票")

    # close all webs
    def close(self):
        self.context.close()
        self.browser.close()


# module 1:
# Hotel recommendation
print("酒店推荐")
with sync_playwright() as playwright:

    # case1: varity the recommended hotel on the current page
    print("case1 验证结果：")
    recommendedHotel = TourHotel(playwright)
    recommendedHotel.navigate_to_page()
    recommendedHotel.maximize_window()
    recommendedHotel.click_module("酒店 按回车键打开菜单")
    recommendedHotel.varity_area_name("酒店推荐")
    recommendedHotel.varity_hotel()
    recommendedHotel.close()

    # case2: varity the recommended regions on the current page
    print("case2 验证结果：")
    recommendedArea = TourHotel(playwright)
    recommendedArea.navigate_to_page()
    recommendedArea.maximize_window()
    recommendedArea.click_module("酒店 按回车键打开菜单")
    recommendedArea.varity_area_name("酒店推荐")
    recommendedArea.varity_theSelectedAreaNumber()
    recommendedArea.close()

# module 2:
# Hot push in the season
print("当季热推")
with sync_playwright() as playwright:

    # case1: Hot push in the season - Package tour
    print("case1 验证结果：")
    SeasonPush = TourHotel(playwright)
    SeasonPush.navigate_to_page()
    SeasonPush.maximize_window()
    SeasonPush.click_module("酒店 按回车键打开菜单")
    SeasonPush.varity_area_name("当季热推")
    SeasonPush.varity_area_name("当季热卖·跟团游")
    SeasonPush.varity_tour()
    SeasonPush.close()

    # case2: dscounted airfare
    print("case2 验证结果：")
    # In order to enlarge the window, start the non-headless mode
    Ticket = TourHotel(playwright, headless=False)
    Ticket.navigate_to_page()
    Ticket.maximize_window()
    Ticket.click_module("酒店 按回车键打开菜单")
    Ticket.varity_area_name("当季热卖·跟团游")
    Ticket.varity_area_name("周末畅游·特价机票")
    Ticket.varity_airlineTicket("div.pas_recommend-container_2uDvk > div.pas_flight_LCrXO > ul.pas_r-ul_ZTteF > li:nth-child(1) a","不限舱等")
    Ticket.close()