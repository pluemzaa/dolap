def main():
    print("===== Calculate Grade Program =====")
    students = []
    grades = []
    idx = 1

    while True:
        # รับชื่อ
        name = input(f"Enter student name No.{idx} : ").strip()
        while not name:
            name = input(f"Enter student name No.{idx} : ").strip()

        # รับเกรด (ตัวเลขทศนิยม)
        while True:
            try:
                grade = float(input("Enter Grade : ").strip())
                break
            except ValueError:
                continue  # ถ้าไม่ใช่ตัวเลข ให้ถามซ้ำ

        students.append(name)
        grades.append(grade)

        # ถามว่าจะทำต่อหรือไม่
        cont = input("Continue? (y/n) : ").strip().lower()
        while cont not in ("y", "n"):
            cont = input("Continue? (y/n) : ").strip().lower()

        if cont == "n":
            break

        idx += 1

    # สรุปผล
    print("\n===== Report =====")
    if grades:
        avg = sum(grades) / len(grades)
        max_index = max(range(len(grades)), key=lambda i: grades[i])
        min_index = min(range(len(grades)), key=lambda i: grades[i])
        print(f"Average : {avg:.2f}")
        print(f"Max : {students[max_index]}")
        print(f"Min : {students[min_index]}")
    else:
        print("Average : 0.00")
        print("Max : -")
        print("Min : -")

if __name__ == "__main__":
    main()