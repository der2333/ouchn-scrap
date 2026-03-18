import sys

import questionary

from src.browser import start_browser


def print_header() -> None:
    print("\n" + "=" * 50)
    print("       OUCHN SCRAPER")
    print("=" * 50 + "\n")


def batch_download_homework() -> None:
    choice: str = questionary.select(
        "请选择课程范围:",
        choices=[
            questionary.Choice(title="所有课程(班主任)", value="all"),
            questionary.Choice(title="指定课程", value="specific"),
            questionary.Choice(title="返回", value="back"),
        ],
    ).ask()

    if choice == "back":
        return

    if choice == "all":
        print("\n[批量下载形考作业答案] - 所有课程(班主任)")
    else:
        course_name: str = questionary.text("请输入课程名称:").ask()
        if not course_name:
            print("\n课程名称不能为空。\n")
            return
        print(f"\n[批量下载形考作业答案] - 课程: {course_name}")

    username: str = questionary.text("请输入账号:").ask()
    if not username:
        print("\n账号不能为空。\n")
        return

    password: str = questionary.password("请输入密码:").ask()
    if not password:
        print("\n密码不能为空。\n")
        return

    print(f"\n账号: {username}")
    start_browser(username, password)
    print("下载完成！\n")


def main() -> int:
    print_header()

    while True:
        choice: str = questionary.select(
            "请选择操作:",
            choices=[
                "批量下载形考作业答案",
                "退出",
            ],
        ).ask()

        if choice == "退出":
            return 0
        elif choice == "批量下载形考作业答案":
            batch_download_homework()


if __name__ == "__main__":
    sys.exit(main())
