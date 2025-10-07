calories = 0.06
try:
    steps = int(input("Enter the number of steps taken: "))
    if steps < 0:
        print("Number of steps cannot be negative. Please enter a valid number.")
    else:
        calories_burned = steps *  calories
        print("Total calories burned: %.2f calories" % calories_burned)