def print_multiplication_table(num):
  """
  แสดงสูตรคูณของเลขที่รับเข้ามา

  Args:
    num: ตัวเลขที่ต้องการแสดงสูตรคูณ
  """
  for i in range(1, 13):
    result = num * i
    print(f"{num} x {i} = {result}")

# รับค่าจากผู้ใช้
try:
  number = int(input("ป้อนตัวเลขเพื่อแสดงสูตรคูณ: "))
  print_multiplication_table(number)
except ValueError:
  print("ป้อนข้อมูลไม่ถูกต้อง กรุณาป้อนตัวเลข")