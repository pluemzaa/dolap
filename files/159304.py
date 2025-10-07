num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")

a=num1+num2
b=num1-num2
c=num1*num2
d=num1/num2

if op == "+":
    print(f"Resut: {a:.2f}")
elif op == "-":
    print(f"Resut: {b:.2f}")
elif op == "*":
    print(f"Resut: {c:.2f}")
elif op == "/":
    print(f"Resut: {d:.2f}")

else:
    print("Invalid operator")