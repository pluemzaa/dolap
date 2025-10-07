weight = float(input('Enter your weight (kg):'))
height = float(input('Enter your height (m):'))
BMI = (weight/height**2)

if weight <= 0 or height <=0:
    print('Invalid input')
elif BMI < 18.5:
    print(f'Your BMI is: {BMI:.2f}')
    print('Category: Underweight')
elif 18.5 <= BMI < 25 :
    print(f'Your BMI is: {BMI:.2f}')
    print('Category: Normal weight')
elif 25 <= BMI < 30 :
    print(f'Your BMI is: {BMI:.2f}')
    print('Category: Overweight')
elif BMI >= 30 :
    print(f'Your BMI is: {BMI:.2f}')
    print('Category: Obese')