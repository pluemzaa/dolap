ans = 42
Gues = ""
while Gues!=ans :
  Gues = int(input("Guess the number (between 1 and 99):"))
  if Gues==ans :
    print("Congratulations! You guessed the number")
  elif Gues>ans :
    print("Too high!")
  else:
    print("Too low!")