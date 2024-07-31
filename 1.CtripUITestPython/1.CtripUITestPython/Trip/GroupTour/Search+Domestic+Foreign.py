# @summary --- Jinyu Sun
# 1.Verity the Search feature in the group tour
    # Open XieCheng web
    # Switch to the group tour module
    # Click "Search" to search for "哈尔滨"
    # Select a few options about the tour
    # Click the first search result --> Verify that you can be redirected to the corresponding web page
# 2.Verify the domestic tour in the group tour
    # Open XieCheng web
    # Switch to the group tour module
    # Verify that the recommended location is domestic
    # Click on recommended domestic travel items --> Verify that you can be redirected to the corresponding web page
# 3.Verify the abroad tour in the group tour
    # Open XieCheng web
    # Switch to the group tour module
    # Verify that the recommended location is foreign
    # Click on recommended foreign travel items --> Verify that you can be redirected to the corresponding web page


from playwright.sync_api import Playwright, sync_playwright, expect

class Tour:
    def __init__(self, playwright: Playwright, headless: bool = False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()

    # Open the tested web
    def navigate_to_page(self, url):
        self.page = self.context.new_page()
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    # Switch to the tested module -> 跟团游
    def click_group_tour(self):
        self.page.locator(".pc_home-tabbtnIcon").click()
        self.page.get_by_role("link", name="跟团游", exact=True).click()
        self.page.wait_for_load_state("networkidle")

    # search a location -> 哈尔滨
    def search(self):
        self.page.get_by_label("请输入目的地、主题或关键字").click()
        self.page.get_by_label("请输入目的地、主题或关键字").fill("哈尔滨")
        self.page.get_by_label("请输入目的地、主题或关键字").press("Enter")
        self.page.wait_for_load_state("networkidle")

    # Select some information in the search results
    def search_result_information(self):
        self.page.get_by_text("哈尔滨一地")
        self.page.locator("#filter_box_point").get_by_text("南京").click()
        self.page.get_by_text("7日", exact=True).click()
        self.page.get_by_text("明天").click()
        self.page.wait_for_load_state("networkidle")

    # Varity a tour in the search result
    def search_result_tour(self, search_TourName, search_HeadingName):
        with self.page.expect_popup() as page2_info:
            self.page.get_by_text(search_TourName).first.click()
            page2 = page2_info.value
            self.page.wait_for_load_state("networkidle")
            element = page2.get_by_role("heading", name=search_HeadingName)
        assert element is not None, "验证失败"
        print("搜索，验证成功")

    # Varity whether the address name belongs to the current module
    def verify_region_texts(self, xpath, file_path):
        em_elements = self.page.locator(xpath)
        em_texts = []
        for i in range(em_elements.count()):
            em_texts.append(em_elements.nth(i).text_content())
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            for text in em_texts:
                assert text in file_content, f"验证失败: {text} 不符合要求"
                print(f"验证成功: {text} 符合要求")

    #Select a tour and verify that it is accessible
    def select_tour_and_verify(self, tour_name, heading_name):
        with self.page.expect_popup() as popup_info:
            self.page.get_by_role("link", name=tour_name).first.click()
        page1 = popup_info.value
        page1.wait_for_load_state("networkidle")
        assert page1.get_by_role("heading", name=heading_name) is not None, "验证失败"
        print("成功访问")

    def close(self):
        self.context.close()
        self.browser.close()

# search
with sync_playwright() as playwright:
    Tour_Search = Tour(playwright)
    Tour_Search.navigate_to_page("https://vacations.ctrip.com/")
    Tour_Search.click_group_tour()
    Tour_Search.search()
    Tour_Search.search_result_information()
    Tour_Search.search_result_tour("哈尔滨7日6晚拼小团","哈尔滨7日6晚拼小团")
    Tour_Search.close()

# the domestic tour
with sync_playwright() as playwright:
    print("境内游测试结果：")
    Tour_Inland = Tour(playwright)
    Tour_Inland.navigate_to_page("https://vacations.ctrip.com/")
    Tour_Inland.click_group_tour()
    # The address of the inland.txt file needs to be changed accordingly during verification
    Tour_Inland.verify_region_texts('div.group_mod.group_inland.basefix > div.group_con_r > div.group_text_nav > div.group_text_col em', r'D:\Program files\Auto\CodeDate\Jinyu\Auto_XieChengWeb\inland.txt')
    Tour_Inland.select_tour_and_verify("海南三亚5日4晚跟团游","海南三亚5日4晚跟团游")
    Tour_Inland.close()

# the foreign tour
with sync_playwright() as playwright:
    print("境外游测试结果：")
    Tour_Foreign = Tour(playwright)
    Tour_Foreign.navigate_to_page("https://vacations.ctrip.com/")
    Tour_Foreign.click_group_tour()
    # The address of the foreign.txt file needs to be changed accordingly during verification
    Tour_Foreign.verify_region_texts('div.group_mod.group_foreign.basefix > div.group_con_r > div.group_text_nav > div.group_text_col em', r'D:\Program files\Auto\CodeDate\Jinyu\Auto_XieChengWeb\foreign.txt')
    Tour_Foreign.select_tour_and_verify("新加坡+马来西亚5日4晚私家团", "新加坡+马来西亚5日4晚私家团")
    Tour_Foreign.close()
