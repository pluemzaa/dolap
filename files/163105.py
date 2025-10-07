def solve_pyramid_puzzle():
    """
    ฟังก์ชันหลักในการแก้ไขปริศนาพีระมิดวิทยวิภาส
    """
    try:
        # ภารกิจที่ 1: รับค่าความสูงของพีระมิด (N) จากผู้กล้า
        n_str = input("Enter the number of rows for the pyramid: ")
        n = int(n_str)

        # ตรวจสอบเงื่อนไข 1 <= N <= 50
        if not (1 <= n <= 50):
            print("ท่านผู้กล้า โปรดป้อนจำนวนเต็มบวกระหว่าง 1 ถึง 50")
            return

        # ภารกิจที่ 2: คำนวณจำนวนกล่องทั้งหมด
        # ใช้สูตรผลรวมของอนุกรมเลขคณิต: n * (n + 1) / 2
        total_boxes = n * (n + 1) // 2
        print(f"The total number of boxes: {total_boxes}")

        # ภารกิจที่ 3: ตรวจสอบว่าเป็นเลขคู่หรือคี่ และกำหนดทิศทางของพีระมิด
        if total_boxes % 2 == 0:
            # กรณีเลขคู่: พิมพ์พีระมิดแบบปกติ (1 ถึง N)
            print("The total number of boxes is even")
            pyramid_range = range(1, n + 1)
        else:
            # กรณีเลขคี่: พิมพ์พีระมิดแบบกลับหัว (N ถึง 1)
            print("The total number of boxes is odd")
            pyramid_range = range(n, 0, -1)
        
        # ภารกิจที่ 4: แสดงผลพีระมิดตามเงื่อนไข
        for i in pyramid_range:
            # สร้างรายการของตัวเลขในแถวนั้นๆ
            # เช่น i = 3 จะได้ ['3', '3', '3']
            row_items = [str(i)] * i
            
            # นำรายการมาเชื่อมกันด้วยช่องว่างแล้วพิมพ์ออกมา
            # เช่น ['3', '3', '3'] จะกลายเป็น "3 3 3"
            print(" ".join(row_items))

    except ValueError:
        print("ท่านผู้กล้า โปรดป้อนข้อมูลเป็นตัวเลขจำนวนเต็มเท่านั้น")

# เริ่มต้นภารกิจ!
solve_pyramid_puzzle()