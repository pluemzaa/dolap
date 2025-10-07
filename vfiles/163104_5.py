print("===== Calculate Grade Program =====")

n = 0
list = []

while True:
    n += 1
    
    student = input(f"Enter student name No.{n} : ")
    grade = float(input("Enter Grade : "))
    
    list.append([student,grade])
    
    if input("Continue? (y/n) : ") == "n":
        break
    
a = 0
max = ["",0]
min = False

print("===== Report =====")

for i in range(len(list)):
    v = list[i]
    
    a += v[1]
    
    if v[1] > max[1]:
        max = v
        
    if not min or v[1] < min[1]:
        min = v
        
a /= len(list)

print(f"Average : {a:.2f}")
print(f"Max : {max[0]}")
print(f"Min : {min[0]}")