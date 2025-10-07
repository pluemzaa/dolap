g = 42
num = 0
while num != 42 :
  num = int(input("Guess the number (between 1 and 99):"))
  if num < 42 :
    print("Too low!")
  elif num > 42 :
    print("Too high!")
  else :
    print("Congratulations! You guessed the number")