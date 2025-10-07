KG = float(input("Enter your weight (kg): "))
M =  float(input("Enter your height (m): "))
if KG <= 0 or M <= 0 :
   print("Invalid input")
else:
    bmi = KG/(M**2)
    print("Your BMI is:{:.2f}".format(bmi))
    if bmi < 18.5:
      print("Category:Underweight")
    elif bmi < 25:
       print("Category:Normal weight") 
    elif bmi < 30:
       print("Category:Overweight")   
    elif bmi >= 30:
       print("Category:Obese")