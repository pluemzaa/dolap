key=42
while True:
  n=int(input("Guess the number (between 1 and 99):"))
  if n < key:
    print("Too low!")
  elif n > key:
    print("Too high!")
  else:
    print("Congratulations! You guessed the number")
    break