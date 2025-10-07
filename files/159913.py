total = 0.0
count = -1
N = -1
while N != 0:
  N = int(input('Enter a number (enter 0 to stop):'))
  total += N 
  count += 1
if total == 0 and N == 0:
  print("No numbers were entered.")
else:
  print("Average:",total/count)
text = input("Enter input: ")