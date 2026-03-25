from playwright.sync_api import Locator, BrowserContext, Page, TimeoutError, Response
from ..stealth import init_page
from .download import download


def course_page_reload(course_page: Page) -> None:
    i = 1
    while i <= 5:
        course_jobs = course_page.locator(".title.ng-binding").all()
        if len(course_jobs) > 0:
            break
        else:
            course_page.reload()
            course_page.wait_for_timeout(7000)
            i += 1


def course_handle(course: Locator, ctx: BrowserContext) -> None:
    exams_info: list[dict] = []

    def handle_response(response: Response):
        nonlocal exams_info
        if "all-activities" in response.url:
            json_data: dict = response.json()
            exams_info = [
                {"id": exam["id"], "title": exam["title"]}
                for exam in json_data["exams"]
                if exam.get("is_formative") is True
            ]

    course_page = ctx.new_page()
    init_page(course_page)

    href = course.get_attribute("href")
    if href is None:
        return
    course_id = href.split("/")[2]

    course_page.on("response", handle_response)
    course_page.goto(f"https://lms.ouchn.cn/course/{course_id}/ng#/appraisal-task")
    course_page.wait_for_timeout(10000)
    course_name = course_page.title()[:-9]

    # 让课程页面加载出形考任务
    try:
        course_page_reload(course_page)
    except TimeoutError:
        course_page.close()
        print(f"{course_name}: 页面加载超时，下载失败")

    if exams_info == []:
        print(f"{course_name}: 没有形考任务")
        course_page.close()
        return

    # print(exams_info)

    download(ctx, course_id, course_name, exams_info)

    course_page.close()
