m = int(input())
k = int(input())
n = int(input())

total = (m*k) / n

print( total if total % 1 == 0 else (m*k) // n + 1 )