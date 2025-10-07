w = float(input('Enter weight: '))
s = int(input('Select service: '))

if weight <= 0 or height <= 0:
    print("invalid input")
elif BMI < 18.5:
    print(f"Your BMI is: {BMI:.2f}")   
    print("Catagory: Underweight") 
elif 18.5 <= BMI < 25 :
    print(f"BMI is: {BMI:.2f}")   
    print("Catagory: Normal weight") 
elif 25 <= BMI < 30 :
    print(f"BMI is: {BMI:.2f}")   
    print("Catagory: Overweight")
else: BMI >= 30 :   
    print(f"BMI is: {BMI:.2f}")   
    print("Catagory: Obese")