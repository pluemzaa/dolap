tatol = 0 
count = 0
 
 
while True:
   num = int(input("Enter a numer (Enter 0 to stop):"))
   if num == 0:
    break
  tatol += num
  count += 1
  
if count == 0:
    print("No numbers entered.")
else:
    print("Average:", tatol / count)