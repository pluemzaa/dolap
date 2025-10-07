x=int(input('Enter a number (enter 0 to stop):  '))
z=0
z=z+x
a=0
if x !=0 :
  while x !=0 :
    a=a+1
    x=int(input('Enter a number (enter 0 to stop):  '))
    z=z+x
  print('Average',z/a)
  print(a)
else :
  print('No numbers entered.')