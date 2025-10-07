x = int(input("Enter your weight (kg): "))
y = float(input("Enter your height (m):"))
if x > 0 and y  > 0 :
  BMI = (x/((y)**2))
  print (f'Your BMI is:{BMI:.2f} ')
  if BMI < 18.5 :
      print ("Category: Underweight")
  if BMI >= 18.5 and BMI <25 :
      print ("Category: Normal weight")
  if BMI >= 25  and BMI < 30:
      print ("Category: Overweight")
  if BMI >30 :
      print ("Category: Obese")    
else : 
 print ("Invalid input")