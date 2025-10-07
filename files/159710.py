sum = 0
count =0
while True:
  n =float(input('Enter a number (enter 0 to stop):'))
  if n==0:
    break
  sum +=n
  count+=1

if count>0:
  a =sum / count
  print("Average:",a)
else:
  print("No numbers entered.")