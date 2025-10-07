grads = {}
i = 0
total = 0
print("===== Calculate Grade Program =====")
while True:
    i = i + 1
    print(f"Enter student name No.{i:.0f} :", end = "")
    name = input("")
    grad = float(input("Enter Grade : "))
    total = total + grad
    grads[name] = grad
    con = input("Continue? (y/n) : ")
    if con  == "n":
        break
avr = total / i
Max = max(grads, key=grads.get)
Min = min(grads, key=grads.get)
print()
print("===== Report =====")
print(f"Average : {avr:.2f}")
print("Max : ",Max)
print("Min : ",Min)