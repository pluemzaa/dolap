N = int(input("Enter a number N:"))
I = []
NC = 2
while NC != N:
  D = 2
  NC += 1
  while NC % D != 0:
    D += 1
  if NC == D:
    I.append(NC)
print(f"Prime numbers from 1 to {N} are:")
for x in I:
  print(x)