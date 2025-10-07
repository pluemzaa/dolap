num=input("Enter a series of numbers separated by commas: ")
num=num.split(",")
for i in range(len(num)):
    num[i]=float(num[i])
max=max(num)
min=min(num)
print("Normalized values:")
for i in range(len(num)):
    if max == min:
        print("0.00")
    else:
        x=(num[i]-min)/(max-min)
        print(f"{x:.2f}")