t=c=0;n=1
while n!= 0:
    n = float(input("Enter a number(enter 0 to stop): "))
    if n!= 0:
      t+=n;c+=1
if c > 0:
   print(f"Average:{t/c}")
else:
    print("No numbers entered.")