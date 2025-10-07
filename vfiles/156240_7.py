x=input(”Enter a series of numbers separated by commas: “)
x=x.split(',')
y = list(map(int, x))

m = max(y)

for i in y:
    print(i, ''is the maximum value.'', i == m)