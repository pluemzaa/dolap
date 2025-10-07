n = int(input("Enter the number of rows for the pyramid: "))
print(f"The total number of boxes: {(n * (n + 1))//2}")
if (n * (n + 1) // 2) % 2 == 0:
    t = "even"
else:
    t = "odd"
print(f"The total number of boxes is {t}")

if t == "even":
    for i in range(n):
        for j in range(i + 1):
            print(i + 1, end=" ")
        print()
else:
    for i in range(n):
        for j in range(n - i):
            print(n - i, end=" ")
        print()