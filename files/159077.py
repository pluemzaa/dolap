w  = float(input('Enter your weight (kg): '))
h  = float(input('Enter your height (m): '))

if not ((w <= 0) or (h <=0)):
    BMI = w / (h**2)

    if 0 <= BMI < 18.5:
        print(f'Your BMI is: {BMI:.2f}')
        print('Category: Underweight')
    elif 18.5 <= BMI < 25:
        print(f'Your BMI is: {BMI:.2f}')
        print('Category: Normal weight')
    elif 25 <= BMI < 30:
        print(f'Your BMI is: {BMI:.2f}')
        print('Category: Overweight')
    else:
        print(f'Your BMI is: {BMI:.2f}')
        print('Category: Obese')
else:
    print('Invalid input')