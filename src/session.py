from src.stealth import init_page
from src.download_formative.index import download_formative_homework
from playwright.sync_api import sync_playwright


def start_browser(username: str, password: str, feature: str) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            executable_path="C:\\Users\\13388\\AppData\\Local\\ms-playwright\\chromium-1194\\chrome-win\\chrome.exe",
        )
        ctx = browser.new_context()
        index_page = ctx.new_page()
        init_page(index_page)

        index_page.goto("https://lms.ouchn.cn/user/courses#/")
        index_page.locator('[name="name"]').fill(f"{username}")
        index_page.locator('[name="pwd"]').fill(f"{password}")
        index_page.locator("#agreeCheckBox").click()
        index_page.get_by_role("button", name="登 录").click()

        # 登录成功后根据 feature 调用对应功能
        match feature:
            case "download_formative_homework":
                download_formative_homework(ctx, index_page)

        index_page.wait_for_timeout(4000)
        browser.close()
