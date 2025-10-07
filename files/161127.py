i=0
total=0
while True:
    num=float(input("Enter a number (enter 0 to stop): "))
    if num==0:
        break
        total=total+num
        i=i+1
        if i==0:
            print("No numbers entered.")
        else:
            print(f"Average: {average}")