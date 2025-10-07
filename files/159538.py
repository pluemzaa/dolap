w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
a = "Category:" 
bmi = w/(h**2)
if w <=0:
    print("Invalid input")  
elif h <=0:
        print("Invalid input")  
else: 
    if bmi < 18.5:
        print(f"Your BMI is: {bmi:.2f}")   
        print(a,"Underweight")
    elif bmi <= 25:
        print(f"Your BMI is: {bmi:.2f}")   
        print(a,"Normal weight")
    elif bmi <= 30:
        print(f"Your BMI is: {bmi:.2f}")   
        print(a,"Overweight")
    else:
        print(f"Your BMI is: {bmi:.2f}")   
        print(a,"Obese")