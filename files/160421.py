w=input("Enter a series of numbers separated by commas: ")
w =w.split(",")
0,1,5,5,1,7

for i in range(0,len(w)):
    w[i]=int(w[i])

_w = w[0]
_y = w[0]
for i in range (0,len(w)):
    if w[i] > _w:
        _w = w[i]
        print(f"set the maximum value to {_w}")

print(f"The maximum value is {_w}")