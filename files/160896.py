randnum = 42
while True:
  inr = int(input("Guess the number (between 1 and 99): "))
  if inr > randnum:
    print("Too high!")
  elif inr < randnum:
    print("Too low!")
  else:
    print("Congratulations! You guessed the number")
    break