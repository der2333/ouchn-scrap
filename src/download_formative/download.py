import time
import os
from playwright.sync_api import BrowserContext


def download(
    ctx: BrowserContext, course_id: str, course_name: str, exams_info: list[dict]
) -> None:
    for exam_info in exams_info:
        url = f"https://lms.ouchn.cn/exam/{exam_info.get('id')}/pdf-download?course_id={course_id}&with_answer=true"

        save_dir = f"./形考答案/{course_name}"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        file_path = f"{save_dir}/{exam_info.get('title')}.pdf"

        try:
            # 使用 ctx.request 发送请求，自动使用浏览器上下文的 cookie
            response = ctx.request.get(url, timeout=30000)
            if response.ok:
                with open(file_path, "wb") as f:
                    f.write(response.body())
                print(f"下载完成: {course_name} - {exam_info.get('title')}")
                time.sleep(2)
            else:
                print(
                    f"下载失败: {course_name, exam_info.get('title')}, 状态码: {response.status}"
                )
        except Exception:
            print(f"下载失败: {course_name, exam_info.get('title')}")
