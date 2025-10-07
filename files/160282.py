list = input("Enter a series of numbers separated by commas: ").split(',')

for i in range(len(list)):
    list[i] = int(list[i])

Max = list[0]
for i in range(1, len(list)):
    if list[i] > Max:
        Max = list[i]
        print(f"set the maximum value to {Max}")

print(f"The maximum value is {Max}")