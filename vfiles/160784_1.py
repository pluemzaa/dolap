a=2
while a >1 :
  b =int(input())
  if b > 42:
    print("Too high!")
  elif b ==42:
    print("Congratulations! You guessed the number")
    break
  else:
    print("Too low!")