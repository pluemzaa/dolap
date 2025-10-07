n = int(input("Enter your weight (kg):"))
t = float(input("Enter your height (m):"))
if n <= 0 :
    print("Invalid input")
else:
    b = n/t**2
    print(f"Your BMI is:{b:.2f}")
    if b < 18.5 :
        print("Category:Underweight")  
    if 18.5 <= b < 25 :
        print("Category:Normal weight")
    if 25 <= b < 30 :
        print("Category:Overweight")
    if  b>= 30:
        print("Category:Obese")