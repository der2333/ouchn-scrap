import sys

import questionary

from src.session import start_browser


def print_header() -> None:
    print(f"\n{'=' * 50}")
    print("       OUCHN SCRAPER")
    print(f"{'=' * 50}\n")


def _require_input(prompt: str) -> str | None:
    """返回非空输入，空值时返回 None（由调用方处理返回菜单）"""
    value: str = questionary.text(prompt).ask()
    if not value:
        print("\n输入不能为空\n")
        return None
    return value


# 批量下载形考作业答案
def download_formative_homework_menu() -> None:
    choice: str = questionary.select(
        "请选择课程范围:",
        choices=[
            questionary.Choice(title="所有课程", value="all"),
            questionary.Choice(title="指定课程", value="specific"),
            questionary.Choice(title="返回", value="back"),
        ],
    ).ask()

    if choice == "back":
        return

    course_name: str | None = None
    if choice == "all":
        print("\n[批量下载形考作业答案] - 所有课程")
    else:
        course_name = _require_input("请输入课程名称:")
        if course_name is None:
            return
        print(f"\n[批量下载形考作业答案] - 课程: {course_name}")

    username: str | None = _require_input("请输入一平台账号:")
    if username is None:
        return

    password: str = questionary.password("请输入一平台密码:").ask()
    if not password:
        return

    print(f"\n账号: {username}\n")
    start_browser(
        username, password, "download_formative_homework", choice, course_name or ""
    )


def main() -> int:
    print_header()

    while True:
        choice: str = questionary.select(
            "请选择操作:",
            choices=[
                "批量下载形考作业答案(班主任)",
                "退出",
            ],
        ).ask()

        match choice:
            case "退出":
                return 0
            case "批量下载形考作业答案(班主任)":
                download_formative_homework_menu()


if __name__ == "__main__":
    sys.exit(main())
