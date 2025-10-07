n = int(input("Enter the number of rows for the pyramid: "))

total = n * (n + 1) // 2 print(f"The total number of boxes: {total}") print("The total number of boxes is even" if total % 2 == 0 else "The total number of boxes is odd")

for i in range(1, n + 1): print(" ".join([str(i)] * i))