# Enter item 1 : apple
# Enter weight 1 : 100.2
# Enter item 2 : papaya
# Enter weight 2 : 502.4
# Enter item 3 : banana
# Enter weight 3 : 350.7
# Enter item 4 : orange
# Enter weight 4 : 455.8
# เขียนโปรแกรมรับชื่อผลไม้ และ น้ำหนักของผลไม้ โดยรับผลไม้ทั้งหมด 4 ชนิด 
# และรับทีละบรรทัด จากนั้นแสดงผลรวมน้ำหนักทั้งหมดในบรรทัดสุดท้าย นำมาแสดงผลดังกรณีทดสอบ
data_labels = []
data_values = []

# input
for i in range(4):
    data_labels.append(input(f"Enter item {i+1} : "))
    data_values.append(float(input(f"Enter weight {i+1} : ")))
# out
sum = 0
for i in range(4):
    print(f"{data_labels[i]}\t{data_values[i]:.2f}")
    sum += data_values[i]

print("---------------------------")
print(f"Total\t{sum:.2f}")