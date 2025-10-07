x = int(input("Enter your weight (kg): "))
y = float(input("Enter your height (m):"))
if x&y > 0 :
 BMI = x/((y)**2)
 print (f'Your BMI is:{BMI:.2f} ')
if BMI < 18.5 :
      print ("Underweight")
if BMI <= 18.5 & BMI <25 :
      print ("Normal weight")
if BMI <= 25  & BMI < 30:
      print ("Overweight")
if BMI >30 :
      print ("Obese")    
else :
 print ("Invalid input")