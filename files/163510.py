num1 = int(input(""))
num2 = int(input(""))
num3 = int(input(""))
total = num1 * num2
total_1 = total // num3
if total % num3 > 0:
    total_1 += 1
print(total_1)