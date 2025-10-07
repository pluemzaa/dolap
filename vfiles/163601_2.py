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
  print("Average :",avg)
  math.ceil(avg)
  max_ppl = gpa.index(max(gpa))
  min_ppl = gpa.index(min(gpa))
  print("Max :",max_ppl)
  print("Min :",min_ppl)
  break