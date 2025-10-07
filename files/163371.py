# -*- coding: utf-8 -*-

def read_float(prompt: str) -> float:
    """Read a float with validation (expects 0.00–4.00)."""
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
            if 0.0 <= value <= 4.0:
                return value
            else:
                print("กรุณาใส่เกรดระหว่าง 0.00 ถึง 4.00")
        except ValueError:
            print("กรุณาใส่ตัวเลข เช่น 3.50")

def main():
    print("===== โปรแกรมคำนวณเกรด =====")
    students: list[dict] = []
    index = 1

    while True:
        name = input(f"ใส่ชื่อนักเรียน หมายเลข {index} : ").strip()
        grade = read_float("ใส่เกรด : ")
        students.append({"name": name, "grade": grade})

        cont = input("ดำเนินการต่อหรือไม่ (y/n) : ").strip().lower()
        if cont != "y":
            break
        index += 1

    if not students:
        print("\n===== รายงาน =====")
        print("ไม่มีข้อมูลนักศึกษา")
        return

    # Compute statistics
    total = sum(s["grade"] for s in students)
    avg = total / len(students)

    highest = max(students, key=lambda s: s["grade"])
    lowest = min(students, key=lambda s: s["grade"])

    # Output (with a blank line before the report)
    print()
    print("===== รายงาน =====")
    print(f"เฉลี่ย : {avg:.2f}")
    print(f"สูงสุด : {highest['name']}")
    print(f"ต่ำสุด : {lowest['name']}")

if __name__ == "__main__":
    main()