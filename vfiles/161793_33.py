n = int(input("Enter number :"))
if n < 1 :
   print("Error number must be 1 or graeter")
else :
  for step in range(1, n + 1):
      stars = '*' * (2 * step)
      for _ in range (2):
          print(stars)