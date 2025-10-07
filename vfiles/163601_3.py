import math
ans = "y" 
n = 1 
people = ""
members = []
gpa = []
avg = 0
max_ppl = ''
min_ppl = ''

print("===== Calculate Grade Program =====")

while ans == "y":
  people = input(f"Enter student name No.{n} : ")
  members.append(people)
  grade = float(input("Enter Grade : "))
  gpa.append(grade)
  n += 1
  ans = input("Do you want to continue? (y/n) : ")
  
while ans == "n":
  print()
  print()
  print("===== Report =====")
  avg = sum(gpa)/len(members)
  print(f"Average :{avg:.2f}")
  math.ceil(avg)
  max_ppl = gpa.index(max(gpa))
  min_ppl = gpa.index(min(gpa))
  print(f"Max :{members[max_ppl]}")
  print(f"Min :{members[min_ppl]}")
  break