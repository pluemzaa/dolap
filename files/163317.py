n = int(input("Enter the number of rows for the pyramid: "))

t = n * (n + 1) // 2

print(f"The total number of boxes: {t}")


if t % 2 == 0:
    print("The total number of boxes is even")
else:
    print("The total number of boxes is odd")


for i in range(1, n + 1):

    print(str(i) * i)