from playwright.sync_api import Playwright, sync_playwright, expect

def search(playwright: Playwright) -> None:
    browse = playwright.chromium.launch(headless=False)
    context = browse.new_context()
    page = context.new_page()
    page.goto("https://vacations.ctrip.com/")
    page.wait_for_load_state("networkidle")
    
    # 跟团游
    page.locator(".pc_home-tabbtnIcon").click()
    page.get_by_role("link", name="跟团游", exact=True).click()
    page.wait_for_load_state("networkidle")
    
    # 搜索 哈尔滨
    page.get_by_label("请输入目的地、主题或关键字").click()
    page.get_by_label("请输入目的地、主题或关键字").fill("哈尔滨")
    page.get_by_label("请输入目的地、主题或关键字").press("Enter")
    page.wait_for_load_state("networkidle")
    
    #选择相关信息
    page.get_by_text("哈尔滨一地")
    page.locator("#filter_box_point").get_by_text("南京").click()
    page.get_by_text("7日", exact=True).click()
    page.get_by_text("明天").click()
    page.wait_for_load_state("networkidle")
    
    #选择对应旅游团
    with page.expect_popup() as page2_info:
        page.get_by_text("哈尔滨7日6晚拼小团").first.click()
    page2 = page2_info.value
    page.wait_for_load_state("networkidle")
    
    # 断言
    element = page2.get_by_role("heading", name="哈尔滨7日6晚拼小团")
    assert element is not None, "验证失败"
    print("验证成功")
    
    context.close()
    browse.close()

with sync_playwright() as playwright:
    search(playwright)