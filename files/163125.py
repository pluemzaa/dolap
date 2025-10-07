def draw_pyramid(n, inverted=False, symbol='*'):
    if inverted:
        rng = range(n, 0, -1)
    else:
        rng = range(1, n + 1)
    for i in rng:
        print(symbol * i)

def main():
    try:
        n = int(input("ป้อนค่า N (1-50): ").strip())
    except ValueError:
        print("ข้อมูลนำเข้าไม่ถูกต้อง")
        return

    if not (1 <= n <= 50):
        print("ข้อมูลนำเข้าไม่อยู่ในช่วงที่กำหนด (1-50)")
        return

    total = n * (n + 1) // 2  # จำนวนกล่องทั้งหมด

    print(f"จำนวนกล่องทั้งหมด: {total}")
    if total % 2 == 0:
        print("ผลรวมเป็นเลขคู่ -> แสดงพีระมิดปกติ")
        draw_pyramid(n, inverted=False, symbol='*')
    else:
        print("ผลรวมเป็นเลขคี่ -> แสดงพีระมิดกลับหัว")
        draw_pyramid(n, inverted=True, symbol='*')

if __name__ == "__main__":
    main()