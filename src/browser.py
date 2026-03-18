from playwright.sync_api import sync_playwright


def start_browser(username: str, password: str) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # TODO: 实现登录和下载逻辑
        page.goto("https://lms.ouchn.cn/user/courses#/")
        page.wait_for_timeout(5000)
        browser.close()
