n=int(input("Enter a number (enter 0 to stop):"))
numbers = [] 
while n!=0:
  numbers.append(n) 
  n=int(input("Enter a number (enter 0 to stop):"))
if n==0: 
  print("No numbers entered.")
else:
  Average = sum(numbers)/len(numbers) 
  print("Average",Average)