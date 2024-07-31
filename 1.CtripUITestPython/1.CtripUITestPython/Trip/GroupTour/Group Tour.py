# @summary --- Jinyu Sun
# The Group Tour:
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

    # 3.Verify the surrounding tour in the group tour
        # Open XieCheng web
        # Switch to the group tour module
        # Verify that the recommended location is the surrounding area
        # Click on recommended surrounding tour items --> Verify that you can be redirected to the corresponding web page

# The Study Tour:
    # 1.Varity Parent-child activities
        # Varity the main page feature of the parent-child activities in study tour
            # Open XieCheng web
            # Switch to the study tour module
            # Verify that the recommended location is activity area
            # Click on recommended items --> Verify that you can be redirected to the corresponding web page
        # Varity the more options feature of the parent-child activities in study tour
            # Open XieCheng web
            # Switch to the study tour module
            # Click the More Options button
            # Select some information about tour
            # Click on recommended items --> Verify that you can be redirected to the corresponding web page


from playwright.sync_api import Playwright, sync_playwright, expect

class Tour:
    def __init__(self, playwright: Playwright, headless: bool = False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()

    # Open the tested web
    def navigate_to_page(self):
        self.page = self.context.new_page()
        self.page.goto("https://vacations.ctrip.com/")
        self.page.wait_for_load_state("networkidle")

    # Switch to the tested module
    def click_tour(self, moduleName):
        self.page.locator(".pc_home-tabbtnIcon").click()
        self.page.get_by_role("link", name=moduleName, exact=True).click()
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
        self.page.wait_for_load_state("networkidle")
        self.page.locator("#filter_box_point").get_by_text("南京").click()
        self.page.get_by_text("3日", exact=True).click()
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

    # Tour module：Varity whether the address name belongs to the current module
    def groupTour_region_texts(self, xpath, file_path):
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

    # StudyTour module:Varity whether the address name belongs to the current module
    def studyTour_region_texts(self, xpath, file_path):
        span_elements = self.page.locator(xpath)
        span_texts = []
        for i in range(span_elements.count()):
            span_texts.append(span_elements.nth(i).text_content())
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            for text in span_texts:
                assert text in file_content, f"验证失败: {text} 不符合要求"
                print(f"验证成功: {text} 符合要求")

    # Varity more option module
    def more_options(self, xpath):
        with self.page.expect_popup() as page2_info:
            self.page.locator(xpath).click()
        page2 = page2_info.value
        page2.get_by_text("亲子", exact=True).first.click()
        page2.get_by_text("1日", exact=True).click()
        page2.get_by_text("明天").click()
        page2.locator("#filter_box_point").get_by_text("上海").click()

    # close the webs
    def close(self):
        self.context.close()
        self.browser.close()

# search
with sync_playwright() as playwright:
    Tour_Search = Tour(playwright)
    Tour_Search.navigate_to_page()
    Tour_Search.click_tour("跟团游")
    Tour_Search.search()
    Tour_Search.search_result_information()
    Tour_Search.search_result_tour("哈尔滨3日2晚跟团游","哈尔滨3日2晚跟团游")
    Tour_Search.close()

# the domestic tour
with sync_playwright() as playwright:
    print("境内游测试结果：")
    Tour_Inland = Tour(playwright)
    Tour_Inland.navigate_to_page()
    Tour_Inland.click_tour("跟团游")
    # The address of the inland.txt file needs to be changed accordingly during verification
    Tour_Inland.groupTour_region_texts('div.group_mod.group_inland.basefix > div.group_con_r > div.group_text_nav > div.group_text_col em', r'D:\Program files\Auto\CodeDate\Jinyu\Auto_XieChengWeb\GroupTour\inland.txt')
    Tour_Inland.select_tour_and_verify("海南三亚5日4晚跟团游","海南三亚5日4晚跟团游")
    Tour_Inland.close()

# the foreign tour
with sync_playwright() as playwright:
    print("境外游测试结果：")
    Tour_Foreign = Tour(playwright)
    Tour_Foreign.navigate_to_page()
    Tour_Foreign.click_tour("跟团游")
    # The address of the foreign.txt file needs to be changed accordingly during verification
    Tour_Foreign.groupTour_region_texts('div.group_mod.group_foreign.basefix > div.group_con_r > div.group_text_nav > div.group_text_col em', r'D:\Program files\Auto\CodeDate\Jinyu\Auto_XieChengWeb\GroupTour\foreign.txt')
    Tour_Foreign.select_tour_and_verify("新加坡+马来西亚5日4晚私家团", "新加坡+马来西亚5日4晚私家团")
    Tour_Foreign.close()

# Tours in the surrounding area
with sync_playwright() as playwright:
    print("周边测试结果：")
    Tour_Surround = Tour(playwright)
    Tour_Surround.navigate_to_page()
    Tour_Surround.click_tour("跟团游")
    # The address of the foreign.txt file needs to be changed accordingly during verification
    Tour_Surround.groupTour_region_texts('div.group_mod.group_surround.basefix > div.group_con_r > div.group_text_nav > div.group_text_col em', r'D:\Program files\Auto\CodeDate\Jinyu\Auto_XieChengWeb\GroupTour\surround.txt')
    Tour_Surround.select_tour_and_verify("苏州+乌镇+杭州3日2晚跟团游", "苏州+乌镇+杭州3日2晚跟团游")
    Tour_Surround.close()

# Parent-child activities
with sync_playwright() as playwright:
    print("亲子活动测试结果：")
    # Main page
    print("主页测试结果：")
    Activity = Tour(playwright)
    Activity.navigate_to_page()
    Activity.click_tour("游学")
    # The address of the inland.txt file needs to be changed accordingly during verification
    Activity.studyTour_region_texts('div.student.box_white > div.vacation_bd.anchor_flag > div.hTitle.hTitle_blue > div.ulTags span', r'D:\Program files\Auto\CodeDate\Jinyu\Auto_XieChengWeb\GroupTour\ActivityArea.txt')
    Activity.select_tour_and_verify("博物馆讲解·【玩转自博馆】上海自然博物馆1","博物馆讲解·【玩转自博馆】上海自然博物馆1")
    Activity.close()
    # More options
    print("更多选项测试结果：")
    ActivityMore = Tour(playwright)
    ActivityMore.navigate_to_page()
    ActivityMore.click_tour("游学")
    ActivityMore.more_options('div.student.box_white > div.vacation_bd.anchor_flag > div.hTitle.hTitle_blue > div.ulTags a')
    ActivityMore.select_tour_and_verify("户外活动·松江浦江之首1","户外活动·松江浦江之首1")
    Activity.close()