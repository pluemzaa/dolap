N = int(input('Enter a number N:'))
txt = 'Prime numbers from 1 to {} are:'.format(N)
print(txt)
for i in range(2,N+1):
  for j in range(2,i+1):
    if i % j == 0 and j != i:
      break
    elif i % j == 0 and j == i:
      print(i)