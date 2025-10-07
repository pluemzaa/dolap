Weigh = int(input('Enter your weight (kg):'))
High=float(input('Enter your height (m):'))
bmi=Weigh/(High)**2

if bmi>0 and High>0 :
    if bmi <18.5:
        print(f'Your BMI is: {bmi:.2f}')
        print('Category: Underweight')
    elif bmi <25:
        print(f'Your BMI is: {bmi:.2f}')
        print('Category: Normal weight')
    elif bmi <30:
        print(f'Your BMI is: {bmi:.2f}')
        print('Category:Overweight ')
    else:
        print(f'Your BMI is: {bmi:.2f}')
        print('Category: Obese')
else:
    print('Invalid input')