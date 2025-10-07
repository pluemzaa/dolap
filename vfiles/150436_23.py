steps = int(input("Enter the number of steps taken: "))  

calories_per_step = 0.06  # แคลอรีที่เผาผลาญต่อก้าว
total_calories = steps * calories_per_step

# แสดงผลลัพธ์แบบมีทศนิยม 2 ตำแหน่ง
print("Total calories burned: %.2f calories" % total_calories)