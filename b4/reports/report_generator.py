from utils.score_utils import calculate_average
from rich.console import Console
from rich.table import Table
console = Console()

from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)



def color_level(level):
    if level == "Giỏi":
        return "[green]Giỏi[/green]"
    elif level == "Khá":
        return "[yellow]Khá[/yellow]"
    elif level == "Trung bình":
        return "[orange1]Trung bình[/orange1]"
    else:
        return "[red]Yếu[/red]"

def display_student_scores(records):
    table = Table(title="Bảng điểm sinh viên")

    columns = ["Mã sinh viên", "Tên", "Điểm trung bình", "Phân loại"]

    for col in columns:
            table.add_column(col.upper(), justify="center")

    for r in records:
        avg, level = calculate_average(*r["scores"])

        table.add_row(
            r["student_id"],
            r["name"],
            str(avg),
            color_level(level)
        )
    
    console.print(table) 


def export_learning_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)
    passed_students = 0
    failed_students = 0

    for student in records:
        avg, _ = calculate_average(*student["scores"])

        if avg >= 5:
            passed_students += 1
        else:
            failed_students += 1

    created_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("learning_report.txt", "w", encoding="utf-8") as file:
        file.write(f"""===== BÁO CÁO HỌC TẬP =====
    Thời gian tạo báo cáo: {created_time}
    Tổng số sinh viên: {total_students}
    Số sinh viên đạt yêu cầu: {passed_students}
    Số sinh viên cần cải thiện: {failed_students}
    """)

    print(f"""
--- XUẤT BÁO CÁO HỌC TẬP ---
Tổng số sinh viên: {total_students}
Số sinh viên đạt yêu cầu: {passed_students}
Số sinh viên cần cải thiện: {failed_students}
""")

    print(
        Fore.GREEN
        + ">> Đã xuất báo cáo ra file learning_report.txt"
        + Style.RESET_ALL
    )