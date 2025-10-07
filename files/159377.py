weight = int(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
BMI = weight/(height**2)
if weight >= 0 and height >= 0 :
    if BMI < 18.5:
        Category = "Underweight"
    if BMI >= 18.5:
        Category = "Normal weight"
    if BMI >= 25:
        Category = "Overweight"
    if BMI >= 30:
        Category = "Obese"
    print(f"Your BMI is: {BMI:.2f}")
    print("Category:",Category)
else:
    print ("Invalid input")