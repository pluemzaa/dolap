num = []
i=int(input("Enter a number (enter 0 to stop): "))
while i!=0:
    num.append(i)
    i=int(input("Enter a number (enter 0 to stop): "))
print("Average: "+ str(sum(num) / len(num)))