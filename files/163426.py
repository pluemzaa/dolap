x = int(input())
y = int(input())
z = int(input())

total = (x * y) / z

print( total if total % 1 == 0 else (x * y) // z + 1 )