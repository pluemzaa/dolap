num = []
i=int(input("Enter a number (enter 0 to stop): "))
if i==0:
    print("No numbers entered.")
    exit()
while i!=0:
    num.append(i)
    print("Enter a number (enter 0 to stop): ", end="")
    i=int(input())
print("Average: "+ str(sum(num) / len(num)))