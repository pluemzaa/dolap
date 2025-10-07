print("===== Calculate Grade Program =====")

Number = 0
Total = 0
while True:
    Number += 1
    nname = input(f"Enter student name No.{Number} : ")
    grade = float(input(f"Enter Grade : "))

    x = input("Continue? (y/n) : ")
    Total += grade
    if x == "n":
        break


Average = Total/Number
print()
print("===== Report =====")
print(f"{Average:.2f}")