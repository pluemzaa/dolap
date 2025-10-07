num = 42
x = int(input("Guess the number (between 1 and 99):"))
if x < num:
  print("Too low!")
elif x > num:
  print("Too high!")
else:
  print("Congratulations! You guessed the number")
while x != num:
  x = int(input("Guess the number (between 1 and 99):"))
  if x < num:
  print("Too low!")
elif x > num:
  print("Too high!")
else:
  print("Congratulations! You guessed the number")