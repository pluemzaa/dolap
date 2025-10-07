Num5 = input('Enter a series of numbers separated by commas:')

Num5 = Num5.split(",")

Num5[0] = int(Num5[0])
Num5[1] = int(Num5[1])
Num5[2] = int(Num5[2])
Num5[3] = int(Num5[3])
Num5[4] = int(Num5[4])

maxx = max(Num5)
minx = min(Num5)

print(f' {Num5[0]} is the maximum value:', Num5[0] is maxx )
print(f' {Num5[1]} is the maximum value:', Num5[1] is maxx  )
print(f' {Num5[2]} is the maximum value:', Num5[2] is maxx  )
print(f' {Num5[3]} is the maximum value:', Num5[3] is maxx )
print(f' {Num5[4]} is the maximum value:', Num5[4] is maxx )