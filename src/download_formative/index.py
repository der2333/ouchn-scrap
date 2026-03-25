from playwright.sync_api import Page, BrowserContext, TimeoutError
from .course_handle import course_handle


def download_formative_homework(ctx: BrowserContext, index_page: Page):
    # 选择班主任
    try:
        index_page.locator("#course-role-select_ms").click()
    except TimeoutError:
        print("请先使用浏览器登录一平台后再重试")
        return
    index_page.locator("#ui-multiselect-3-course-role-select-option-3").click()
    index_page.wait_for_timeout(2000)

    # 选择100
    index_page.locator(".select2-choice").click()
    index_page.locator("#select2-result-label-7").click()
    index_page.wait_for_timeout(4000)

    course_list = index_page.locator("a.ng-binding.ng-scope").all()
    for course in course_list:
        course_handle(course, ctx)
