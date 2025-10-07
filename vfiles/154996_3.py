I = int(input('Enter a series of numbers separated by commas: ').split(','))
x = []
for i in range(len(I)):
   x[i] = int(I[i])
for i in range(len(I)):
   print(f"{x[i]} is the maximum value: ", x[i] is max(I))