A = [1,2,3]
B = [4,5,6]
Dp = 0
for i in range(len(A)):
    value = A[i]* B[i]
    Dp += value
print("Dot Product = ",Dp)