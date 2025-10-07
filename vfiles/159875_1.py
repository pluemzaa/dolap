N = float(input("Enter a number (enter 0 to stop):"))
Sum = 0
I = 0
if N == 0:
  print("No numbers entered.")
else:
    while N > 0:
        Sum = Sum + N
        I = I + 1
        N = float(input("Enter a number (enter 0 to stop):"))
    Avg = Sum/I
    print("Average:",Avg)