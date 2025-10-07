print("===== Calculate Grade Program =====")
i = 0

max = 0
min = int("inf")
sum = 0

max_name = ""
min_name = ""
while True :
    i = i + 1 
    name = str(input(f"Enter student name No.{i} : "))
    grade = float(input("Enter Grade : "))
    if grade > max:
        max = grade
        max_name = name 
    
    if grade < min:
        min = grade
        min_name = name
        
    sum = sum + grade
    _continue = input("Continue? (y/n) : ")
    if _continue == "n":
       break

print("===== Report =====")
avg = sum/i 
print(f"Average : {avg:.2f}")
print(f"Max : {max_name}")
print(f"Min : {min_name}")