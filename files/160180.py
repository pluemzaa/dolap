i = input("Enter a series of numbers separated by commas: ").split(',')
for x in range(len(i)):
    i[x] = int(i[x])
sum = i[0]
for x in range(len(i)):
    if i[x] > sum:
        sum = i[x]
        print(f"set the maximum value to {sum}")        
print(f"The maximum value is {sum}")