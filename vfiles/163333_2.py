print("===== Calculate Grade Program =====")
c = 1
t = 0.0
max_g = 0.0
min_g = 0.0
max_n = ""
min_n = ""

while True :
    name = input(f"Enter student name No.{c} : ")
    grade = float(input("Enter Grade : "))
    
    if c == 1 :
        max_g = min_g = grade
        max_n = min_n = name
    else :
        if grade > max_g :
            max_g = grade
            max_n = name
        if grade < min_g :
            min_g = grade
            min_n = name
            
    t += grade
    
    c = input("Continue? (y/n) : ")
    if c != 'y' :
        break
    c += 1
    
avg = t/c

print()
print("===== Report =====")
print(f"Average : {avg:.2f}")
print(f"Max : {max_n}")
print(f"Min : {min_n}")