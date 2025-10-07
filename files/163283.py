order = int(input())
perorder = int(input())
norder = int(input())

result = (order*perorder)/norder

if result != int:
    result += 0.5
    result = int(result)
    print(result)
else:
    result = int(result)
    print(result)