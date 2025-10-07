n1=int(input("Enter a number (enter 0 to stop):"))
i=0
if n1==0:
  print("No numbers entered.")
else:
  
  while True:
    i=i+1
    if n1!=0:
  
       n1=int(input("Enter a number (enter 0 to stop):"))
       are+=n1
       print(are)
    else:
      n=are/i
      print(n)
      break