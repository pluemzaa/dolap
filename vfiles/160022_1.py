x = 42
while True:
  x = int(input("Guess the number (between 1 and 99):"))
  if x < 42:
    print("Too low!")
  elif x > 42:
    print("Too high!")
  else:
    print("Congratulations! You guessed the number")
    break