num=int(input())
total=0
count=0

while num!=0:
  total+=num
  count+=1
  num=int(input())
if count>0:
  average_1=total/count
  print("Average:",average)
else:
  print("No numbers entered.")