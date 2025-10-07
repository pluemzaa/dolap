i = 0
Name = []
Grade = []

print("===== Calculate Grade Program =====")
while True:
      A = input(f"Enter student name No.{i+1} : ")
      B = float(input("Enter Grade : "))
      C = input("Continue? (y/n) : ")
      C = C.lower()
      i += 1
      Name.append(A)
      Grade.append(B)
      if C == "n":
            break
      elif C == "y":
            continue

Gmax = max(Grade)
Gmin = max(Grade)

maxgrade = -1
mingrade = float('inf')
for i in Grade:
      if i > maxgrade:
            maxgrade = i
for i in Grade:
      if i < mingrade:
            mingrade = i

print("===== Report =====")
print(f"Average : {sum(Grade)/len(Grade):.2f}")
print(f"Max : {maxgrade}")
print(f"Min : {mingrade}")