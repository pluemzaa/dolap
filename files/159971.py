R = 42
G = int(input("Guess the number (between 1 and 99):"))
if R != G:
  while R != G or R == G :
    if R < G:
      print("Too high!")
      G = int(input("Guess the number (between 1 and 99):"))
    elif R > G:
      print("Too Low!")
      G = int(input("Guess the number (between 1 and 99):"))
    else :
          print("Congratulations! You guessed the number")
          break
else :
    print("Congratulations! You guessed the number")