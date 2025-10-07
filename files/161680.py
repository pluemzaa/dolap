n = int(input("Enter number: "))
if(n >= 1):
  ctr_row = 1
  for row in range(1,n+1):
      ctr_col = ctr_row
      for col in range(1,n+1):
        if ctr_col >= 10:
          ctr_col = 1
        print(ctr_col,end='')
        ctr_col += 1
      print()
      ctr_row += 1
      if ctr_row >= 10:
          ctr_row = 1
else:
  print("Error number must be 1 or greater")