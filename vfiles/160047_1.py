A=int(input("Guess the number (between 1 and 99):"))
i=42
while A<=99:
  if A<i:
    print("Too low!")
  elif A>i:
    print("Too high!")
  else :
    print("Congratulations! You guessed the number")
  A=int(input("Guess the number (between 1 and 99):"))