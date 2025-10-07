# รับตัวเลขกี่ตัวก็ได้ คั่นด้วย ,
inputs = list(map(int, input("Enter a series of numbers separated by commas: ").split(',')))

# หาค่าสูงสุด
maximum = max(inputs)

# แสดงผลแบบไม่ใช้ for โดยใช้การเข้าถึงทีละตำแหน่ง
print(f"{inputs[0]} is the maximum value: {inputs[0] == maximum}")
print(f"{inputs[1]} is the maximum value: {inputs[1] == maximum}")
print(f"{inputs[2]} is the maximum value: {inputs[2] == maximum}")
print(f"{inputs[3]} is the maximum value: {inputs[3] == maximum}")
print(f"{inputs[4]} is the maximum value: {inputs[4] == maximum}")