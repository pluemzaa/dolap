n = int(input("Enter number:"))

if n < 1:
      print("Error number must be 1 or greater")
else:
      for i in range(n):
       for j in range(2):
            print("*" * ((i+1)*2))