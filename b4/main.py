from rich.console import Console
from rich.prompt import Prompt

from data.students import student_records
from reports.report_generator import display_student_scores,export_learning_report
from utils.string_utils import normalize_student_names
from utils.random_utils import generate_assignment_code as gen


console = Console()


def view_students():
    display_student_scores(student_records)


def normalize_names():
    normalize_student_names(student_records)


def generate_code():
    print(f"""
--- SINH MÃ BÀI TẬP ---
Mã bài tập của bạn là: {gen()}
""")


def export_report():
    export_learning_report(student_records)


def exit_app():
    console.print("[red]Thoát chương trình...[/red]")
    exit()


def main():
    menu = """
===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====

1. Xem danh sách sinh viên và điểm trung bình
2. Chuẩn hóa tên sinh viên
3. Sinh mã bài tập ngẫu nhiên
4. Xuất báo cáo học tập
5. Thoát chương trình
====================================================
"""

    actions = {
        "1": view_students,
        "2": normalize_names,
        "3": generate_code,
        "4": export_report,
        "5": exit_app
    }

    while True:
        console.print(menu)
        
        choice = Prompt.ask(
            "Chọn chức năng (1-5)",
            choices=["1", "2", "3", "4", "5"],
            show_choices=False
        )

        actions[choice]()


if __name__ == "__main__":
    main()
