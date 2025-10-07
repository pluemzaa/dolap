I = input('Enter a series of numbers separated by commas: ').split(',')
x = []
for i in range(len(I)):
   I[i] = int(I[i])
for i in range(len(I)):
   print(f"{I[i]} is the maximum value: ", I[i] is max(I))