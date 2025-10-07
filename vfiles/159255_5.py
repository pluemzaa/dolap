w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
BMI = 0

if  w > 0 and h> 0 :
  BMI = w/(h*h)
  print(f"Your BMI is: {BMI:.2f} ")
else :
    if  w/(h*h) < 18.5 :
        print("Category: Underweight")
    elif  w/(h*h) >= 18.5 and w/(h*h) < 25 :
        print("Category: Normal weight")
    elif  w/(h*h) >= 25 and w/(h*h) < 30 :
        print("Category: Overweight")
  else :
        print("Invalid input")