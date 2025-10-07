I = int(input('Enter a series of numbers separated by commas: ').split(','))
for i in range(len(I)):
   x[i] = int(x[i])
for i in range(len(I)):
   print(f"{x[i]} is the maximum value: ", x[i] is max(I))