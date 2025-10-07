sum = 0
num = int(input("Enter a number (enter 0 to stop):"))
while num != 0:
  sum = sum+num
  num= int(input())
  average = sum/num
  print(average)