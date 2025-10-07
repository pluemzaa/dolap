weight = 0
height = 0
bmi = 0

weight = float(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))


bmi = weight / (height * height)

if bmi<= 0 :
    print("Invalid input")

else :

    print(f"Your BMI is: {bmi:.2f}")
    print("Category: ", end='', flush=True)


    if bmi < 18.5:
        print ("Underweight")
    else:
        if 18.5 <= bmi < 25:
            print("Normal weight")
        else:
            if 25 <= bmi < 30:
                print("Overweight")
            else:
                if bmi >= 30:
                    print("Obese")