print("===== Calculate Grade Program =====")
D = {}
i = 0
q = 1
Ga = 0
Max_G = 0
Min_G = 0
while True:
    Name = input(f"Enter student name No.{q} :")
    Grade = float(input("Enter grade : "))
    cont = input("Continue? (y/n) : ")
    q += 1
    i += 1
    Ga += Grade
    D[Name] = Grade
    
    if cont == "y":
        continue
    else:
        break
avg = Ga/i
Max = max(D, key=D.get)
Min = min(D, key=D.get)
print()
print("===== Report =====")
print(f"Average :{avg:.2f}")
print(f"Max :{Max}")
print(f"Min :{Min}")