A = input("Enter numbers separated by commas: ")
B = int(input("Enter number to search: "))
A = A.split(",")
i = 0
for i in range(len(A)):
    A[i] = int(A[i])

for i in range(len(A)):
    if B == A [i]:
        print(f"Found {B} at index {i}")

if B not in A:
    print(f"No {B} found.")