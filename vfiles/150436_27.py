steps = int(input("Enter the number of steps taken: "))  

caloriesperstep = 0.06  # แคลอรีที่เผาผลาญต่อก้าว
total_calories = steps * caloriesperstep

# แสดงผลลัพธ์แบบมีทศนิยม 2 ตำแหน่ง
print("The total cost is: %.2f calories" % total_calories)