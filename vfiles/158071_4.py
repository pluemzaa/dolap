x = int(input("Guess the number (between 1 and 99): "))
while x != 42:
  if x < 42:
    print("Too low!")
  else:
    print("Too High!")
print("Congratulations! You guessed the number")