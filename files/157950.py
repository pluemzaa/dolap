a = float(input("Enter a number (enter 0 to stop):"))
i=0
sum = 0
while a != 0 :
	i+=1
	sum = sum + a
	a = float(input("Enter a number (enter 0 to stop):"))

if sum != 0:
	print(f"Average:{sum/i :.1f}") 
else :
	print('No numbers entered.')