num = 42
x = int(input("Guess the number (between 1 and 99):"))
while x != num:
  if x < num:
    print("Too low!")
  elif x > num:
    print("Too high!")
  x = int(input("Guess the number (between 1 and 99):"))
print("Congratulations! You guessed the number")