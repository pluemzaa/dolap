n=int(input("Enter a number N:"))
print("Prime numbers from 1 to",n,"are:")
for num in range(2,n+1):
  prime_number=True  
  for i in range(2,num): 
    if (num % i) == 0:
      prime_number=False 
      break 
  if prime_number: 
    print(num)