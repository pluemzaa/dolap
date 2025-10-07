w = int(input("Enter your weight (kg): "))
h = float(input("Enter your hight (m): "))
yourcatagory = ""
if w >= 0 and h >= 0:
    BMI = (w/h**2)
    if BMI < 18.5:
        yourcatagory = "under weight"
    elif BMI >= 18.5 and BMI < 25:
        yourcatagory = "Normal weight"
    elif BMI >= 25 and BMI < 30:
        yourcatagory = "over weight"
    elif BMI >= 30 :
        yourcatagory = "Obese"
    print(f"Your BMI is: {BMI:.2f}")
    print("Catagory:" ,yourcatagory)
else :
    print("Invalid input")