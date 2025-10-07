n = int(input('Enter number: '))
if n < 1 :
    print("Error number must be 1 or greater")
for i in range(n):
    for i in range(1,n+1):
     isus = '*'*(2*i)
     for _ in range(2):
      print(isus)