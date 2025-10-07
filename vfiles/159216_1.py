if wei <= 0 or hei <= 0:
    print("invalid input")
elif BMI < 18.5:
    print(f"Your BMI is: {BMI:.2f}")   
    print("Catagory: Underweight") 
elif 18.5 <= BMI < 25 :
    print(f"Your BMI is: {BMI:.2f}")   
    print("Catagory: Normal weight") 
elif 25 <= BMI < 30 :
    print(f"Your BMI is: {BMI:.2f}")   
    print("Catagory: Overweight")
elif BMI >= 30 :   
    print(f"Your BMI is: {BMI:.2f}")   
    print("Catagory: Obese")