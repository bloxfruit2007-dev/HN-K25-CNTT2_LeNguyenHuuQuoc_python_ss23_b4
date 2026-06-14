def normalize_name(name):
    return " ".join(name.split()).title()


def normalize_student_names(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("--- CHUẨN HÓA TÊN SINH VIÊN ---")

    for student in records:
        student["name"] = normalize_name(student["name"])
        print(f"{student['student_id']}: {student['name']}")

    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")
