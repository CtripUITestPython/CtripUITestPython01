# @summary --- Jinyu Sun
# 1.Varity Parent-child activities
    # Varity the main page feature of the parent-child activities in study tour
        # Open XieCheng web
        # Switch to the study tour module
        # Verify that the recommended location is activity area
        # Click on recommended items --> Verify that you can be redirected to the corresponding web page
    # Varity the more options feature of the parent-child activities in study tour
        # Open XieCheng web
        # Switch to the study tour module
        # Click the More Options button of the parent-child activities
        # Select some information about tour
        # Click on recommended items --> Verify that you can be redirected to the corresponding web page
# 2.Varity Study tour
    # Varity the main page feature of the study tour
        # Open XieCheng web
        # Switch to the study tour module
        # Verify that the recommended location is study tour
        # Click on recommended items --> Verify that you can be redirected to the corresponding web page
    # Varity the more options feature of the study tour
        # Open XieCheng web
        # Switch to the study tour module
        # Click the More Options button of the study tour
        # Select some information about tour
        # Click on recommended items --> Verify that you can be redirected to the corresponding web page
# 3.Varity summer camp
    # Varity the main page feature of the study tour
        # Open XieCheng web
        # Switch to the study tour module
        # Verify that the recommended location is summer camp
        # Click on recommended items --> Verify that you can be redirected to the corresponding web page
    # Varity the more options feature of the summer camp
        # Open XieCheng web
        # Switch to the study tour module
        # Click the More Options button of the summer camp
        # Select some information about tour
        # Click on recommended items --> Verify that you can be redirected to the corresponding web page


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

    # Switch to the tested module -> 游学
    def click_study_tour(self, module):
        self.page.locator(".pc_home-tabbtnIcon").click()
        self.page.get_by_role("link", name=module, exact=True).click()
        self.page.wait_for_load_state("networkidle")

    # Varity name of the current area
    def varity_area_name(self, areaName):
        area = self.page.get_by_role("heading",name = areaName)
        assert area is not None, "验证失败"
        print(f"验证成功：{areaName}存在")

    # Varity whether the address name belongs to the current module
    def verify_region_texts(self, xpath, file_path):
        span_elements = self.page.locator(xpath)
        span_texts = []
        for i in range(span_elements.count()):
            span_texts.append(span_elements.nth(i).text_content())
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            for text in span_texts:
                assert text in file_content, f"验证失败: {text} 不符合要求"
                print(f"验证成功: {text} 符合要求")

    # Select a tour and verify that it is accessible
    def select_tour_and_verify(self, tour_name, heading_name):
        with self.page.expect_popup() as popup_info:
            self.page.get_by_role("link", name=tour_name).first.click()
        page1 = popup_info.value
        page1.wait_for_load_state("networkidle")
        assert page1.get_by_role("heading", name=heading_name) is not None, "验证失败"
        print("成功访问")

    # Varity more option module
    def more_options(self, xpath):
        with self.page.expect_popup() as page2_info:
            self.page.locator(xpath).click()
        page2 = page2_info.value
        page2.wait_for_load_state("networkidle")

    # close all webs
    def close(self):
        self.context.close()
        self.browser.close()


# Parent-child activities
with sync_playwright() as playwright:
    print("亲子活动测试结果：")
    Activity = StudyTour(playwright)
    # Main page
    print("主页测试结果：")
    Activity.navigate_to_page()
    Activity.click_study_tour("游学")
    Activity.varity_area_name("亲子活动")
    # The address of the inland.txt file needs to be changed accordingly during verification
    Activity.verify_region_texts('div.student.box_white > div.vacation_bd.anchor_flag > div.hTitle.hTitle_blue > div.ulTags span', r'D:\Program files\Auto\CodeDate\Jinyu\Auto_XieChengWeb\StudyTour\ActivityArea.txt')
    Activity.select_tour_and_verify("博物馆讲解·【玩转自博馆】上海自然博物馆1","博物馆讲解·【玩转自博馆】上海自然博物馆1")
    Activity.close()
    # More options
    print("更多选项测试结果：")
    ActivityMore = StudyTour(playwright)
    ActivityMore.navigate_to_page()
    ActivityMore.click_study_tour("游学")
    ActivityMore.more_options('div.student.box_white > div.vacation_bd.anchor_flag > div.hTitle.hTitle_blue > div.ulTags a')
    ActivityMore.select_tour_and_verify("科学探索·【航空学院】上海航宇科普中心1日独立营","科学探索·【航空学院】上海航宇科普中心1日独立营")
    Activity.close()

# Study tour
with sync_playwright() as playwright:
    print("游学测试结果")
    ForeignStudy = StudyTour(playwright)
    # Main page
    print("主页测试结果：")
    ForeignStudy.navigate_to_page()
    ForeignStudy.click_study_tour("游学")
    ForeignStudy.varity_area_name("游学")
    # The address of the inland.txt file needs to be changed accordingly during verification
    ForeignStudy.verify_region_texts('div.parent-child.box_white > div.vacation_bd.anchor_flag > div.hTitle.hTitle_brown > div.ulTags span', r'D:\Program files\Auto\CodeDate\Jinyu\Auto_XieChengWeb\StudyTour\ForeignArea.txt')
    ForeignStudy.select_tour_and_verify("名校探访·美国东西海岸14天研学","名校探访·美国东西海岸14天研学")
    ForeignStudy.close()
    # More options
    print("更多选项测试结果：")
    ForeignStudyMore = StudyTour(playwright)
    ForeignStudyMore.navigate_to_page()
    ForeignStudyMore.click_study_tour("游学")
    ForeignStudyMore.more_options('div.parent-child.box_white > div.vacation_bd.anchor_flag > div.hTitle.hTitle_brown > div.ulTags a')
    ForeignStudyMore.select_tour_and_verify("名校探访·美国东西海岸14天研学亲子夏令营","名校探访·美国东西海岸14天研学亲子夏令营")
    ForeignStudyMore.close()

# Summer camp
with sync_playwright() as playwright:
    SummerCamp = StudyTour(playwright)
    print("夏令营测试结果")
    # Main page
    print("主页测试结果：")
    SummerCamp.navigate_to_page()
    SummerCamp.click_study_tour("游学")
    SummerCamp.varity_area_name("夏令营")
    # The address of the inland.txt file needs to be changed accordingly during verification
    SummerCamp.verify_region_texts('div.adult.box_white > div.vacation_bd.anchor_flag > div.hTitle.hTitle_green > div.ulTags span', r'D:\Program files\Auto\CodeDate\Jinyu\Auto_XieChengWeb\StudyTour\SummerCampTour.txt')
    SummerCamp.select_tour_and_verify("亲近自然·含机票【大草原湖畔木屋","亲近自然·含机票【大草原湖畔木屋")
    SummerCamp.close()
    # More options
    print("更多选项测试结果：")
    SummerCampMore = StudyTour(playwright)
    SummerCampMore.navigate_to_page()
    SummerCampMore.click_study_tour("游学")
    SummerCampMore.more_options('div.adult.box_white > div.vacation_bd.anchor_flag > div.hTitle.hTitle_green > div.ulTags a')
    SummerCampMore.select_tour_and_verify("军事营·上海7天夏令营“特战精英”成长营","军事营·上海7天夏令营“特战精英”成长营")
    SummerCampMore.close()