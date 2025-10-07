A = "1 2 3"
B = "4 5 6"
Dp = 0
for i in range(len(A)):
    value = A[i]* B[i]
    Dp += value
print("Enter v1 (space-separated):",A) 
print("Enter v2 (space-separated):",B)
print("Dot Product : ",Dp)