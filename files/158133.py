RN=42
G=input("Guess the number (between 1 and 99):")
G=int(G)
while G != RN:
  if G > RN:
    print("Too high!")
    G=input("Guess the number (between 1 and 99):")
    G=int(G)
  elif G<RN:
    print("Too low!")
    G=input("Guess the number (between 1 and 99):")
    G=int(G)
else:
  print("Congratulations! You guessed the number")