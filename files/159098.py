num =  int(input("Enter your weight (kg): "))
num2 = float(input("Enter your height (m): "))
num2= num2**2
bmi = num / num2
if num>=0 and num2>=0:
                    if bmi<18.5:
                        print(f"Your BMI is: {bmi:.2f}")
                        print("Category: Underweight")
                    elif 18.5 <=bmi < 25:
                        print(f"Your BMI is: {bmi:.2f}")
                        print("Category: Normal weight")
                    elif 25 <= bmi and bmi< 30:
                        print(f"Your BMI is: {bmi:.2f}")
                        print("Category: Overweight")
                    elif bmi>=30:
                        print(f"Your BMI is: {bmi:.2f}")
                        print("Category: Obese")
else:
    print("Invalid input")