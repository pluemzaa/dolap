#BMI < 18.5 → Underweight
#18.5 ≤ BMI < 25 → Normal weight
#25 ≤ BMI < 30 → Overweight
#BMI ≥ 30 → Obese
#หากป้อนน้ำหนักหรือลูกสูง ≤ 0 ให้แสดงข้อความ
#BMI = weight (kg) / (height (m))2
weight = int(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

if weight > 0 and height > 0 :
    BMI = weight / height**2
    print(f"Your BMI is: {BMI:.2f}")
    if BMI  < 18.5 :
        print("Category: Underweight")
    elif 18.5 <= BMI  < 25 :
        print ("Category: Normal weight")
    elif 25 <= BMI < 30 :
        print("Category: Overweight")
    else:
        print ("Category: Obese")
else:
    print("Invalid input")