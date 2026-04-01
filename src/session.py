from src.stealth import init_page
from src.download_formative.index import download_formative_homework
from playwright.sync_api import sync_playwright, TimeoutError


def start_browser(
    username: str,
    password: str,
    feature: str,
    course_choice: str,
    course_name: str,
) -> None:
    with sync_playwright() as p:
        print("正在启动中...")
        browser = p.chromium.launch()
        ctx = browser.new_context()
        index_page = ctx.new_page()
        init_page(index_page)

        try:
            index_page.goto("https://lms.ouchn.cn/user/courses#/")
            index_page.locator('[name="name"]').fill(f"{username}")
            index_page.locator('[name="pwd"]').fill(f"{password}")
            index_page.locator("#agreeCheckBox").click()
            index_page.get_by_role("button", name="登 录").click()
        except TimeoutError:
            print("账号或密码错误，请重试\n")
            browser.close()
            return

        # 登录成功后根据 feature 调用对应功能
        match feature:
            case "download_formative_homework":
                download_formative_homework(ctx, index_page, course_choice, course_name)

        browser.close()
