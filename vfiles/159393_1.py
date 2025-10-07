weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m):")) 

if weight < 18.5:
    print ("Underweight")
else:
    BMI = weight / (height **2)
    print(f"Your BMI  is: {BMI:.2f}")
if BMI <=  18.5 and BMI <=25:
    print("Normal weight")
if BMI <= 25 and BMI <=30:
    print ("Overweight")    
if BMI > 30:
    print("Obese")