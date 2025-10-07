inr = int(input("Enter a number N:"))
start_num = 1
print("Prime numbers from 1 to 20 are:")
while start_num <= inr:
  i=2
  while i < start_num:
    if start_num % i == 0:
      break
    i+=1
  if i == start_num:
    print(i)
  start_num+=1