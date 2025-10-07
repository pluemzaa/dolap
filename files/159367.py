w = float(input('Enter your weight (kg): '))
h = float(input('Enter your height (m): '))
Bmi = w / h**2
if w > 0 and h > 0:
    if Bmi < 18.5:
        print(f'Your BMI is: {Bmi:.2f}')
        print('Category: Underweight')
    elif Bmi < 25:
        print(f'Your BMI is: {Bmi:.2f}')
        print('Category: Normal weight')
    elif Bmi < 30:
        print(f'Your BMI is: {Bmi:.2f}')
        print('Category: Overweight')
    elif Bmi >= 30:
        print(f'Your BMI is: {Bmi:.2f}')
        print('Category: Obese')        
else:
    print('Invalid input')