w = int(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))
BMI = (w / (h**2))
if w > 0 and h > 0:
    print(f"Your BMI is:{BMI:.2f}")   
    if BMI < 18.5:
        bm = "Underweight"
    elif BMI < 25:
        bm = "Normal weight"
    elif BMI < 30:
        bm = "Overweight"
    else:
        bm = "Obese" 
    print("Category:",bm)    
else:
    print("Invalid input")