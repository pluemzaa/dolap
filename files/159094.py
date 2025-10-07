#จากนั้นให้แสดงผลตามช่วงค่าดังนี้:

#BMI < 18.5 → Underweight
#18.5 ≤ BMI < 25 → Normal weight
#25 ≤ BMI < 30 → Overweight
#BMI ≥ 30 → Obese
#หากป้อนน้ำหนักหรือลูกสูง ≤ 0 ให้แสดงข้อความ
#Invalid input
#Enter your weight (kg): 70
#Enter your height (m): 1.75
#Your BMI is: 22.86
#Category: Normal weight

w = int(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
bmi = w/(h**2)
if bmi >= 0:
    if bmi < 18.5:
        print(f"Your BMI is: {bmi:.2f}")
        print("Category: Underweight")
        
    elif 18.5 <= bmi < 25:
        print(f"Your BMI is: {bmi:.2f}")
        print("Category: Normal weight")
    elif 25 <= bmi < 30:
        print(f"Your BMI is: {bmi:.2f}")
        print("Category: Overweight")
    else:
        print(f"Your BMI is: {bmi:.2f}")
        print("Category: Obese")
else:
    print("Invalid input")