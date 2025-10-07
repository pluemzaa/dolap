x = int(input("Enter the number terms: "))
i = [0,1]
for y in range(x-2):
  i.append(i[y]+i[y+1])
print(*i)