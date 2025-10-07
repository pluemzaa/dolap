w = int(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
text = ""
if w > 0 and h > 0:
  sum = w/(h**2)
  if sum < 18.5:
    text = "Underweight"
  elif sum >= 18.5 and sum <25:
    text = "Normal weight"
  elif sum >= 25 and sum < 30:
    text = "Overweight"
  elif sum >= 30:
    text = "Obese"
  print(f"Your BMI is: {sum:.2f}")
  print(f"Category: {text}")
else : 
    print("Invalid input")