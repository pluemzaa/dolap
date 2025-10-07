num = int(input("Enter a Number:"))

if num > 0:
    print("{} is positive".format(str(num)))
elif num == 0:
    print("{} is zero".format(str(num)))
else:
    print("{} is negative".format(str(num)))