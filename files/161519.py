user = int(input("Enter number: "))

if user < 1:
      print("Error number must be 1 or greater")
else:
      for i in range(user):
            for j in range(i+1):
                  print("**", end="")
            print()
            for k in range(i+1):
                  print("**", end="")
            print()