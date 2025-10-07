w = float(input("Enter your weight (kg):"))
H = float(input("Enter your height (m): "))
if H<=0 or w<=0:
    print("Invalid input")
else:BMI = w / (H**2)
print(f"Your BMI is: %.2f"% BMI )
if BMI < 18.5 :
    
    print("Category: Underweight")
if  18.5 < BMI <=25 :
    
    print("Category: Normal weight")
if 25 <= BMI < 30 :
    
    print(" Category: Overweight")
if BMI >= 30 :
 
 print("Category: Obese")