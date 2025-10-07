i = 1
name = []
score = []
n = len(score)

print("===== Calculate Grade Program =====")

while True:
    st_name =input(f"Enter student name No.{i} :")
    i = i + 1
    grade_ = float(input("Enter Grade :"))
    
    name.append(st_name)
    score.append(grade_)
    
    con = input("Continue? (y/n) :")
    if con=='n':
        break

avg = sum(score)/n

print("                ")
print("===== Report =====")
print("Average :",avg)