print("===== Calculate Grade Program =====")
i=0
max=0
min=0
sum=0
max_n=0
min_n=0
while True:
    i=i+1
    n=str(input("Enter student name No.{i} : "))
    g=float(input("Enter Grade :"))
    if grade > max:
        max = grade
        max_n = n
    if grade < min:
        min = grade
        min_n = n
    sum=sum + g
_continue=str(input("Continue? (y/n):"))