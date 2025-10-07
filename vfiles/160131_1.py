avg=0
c_avg=0
while True :
  num=int(input("Enter a number (enter 0 to stop):"))
  if num==0 :
    break
  avg+=num
  c_avg+=1
print(f"Average:{avg/c_avg}")