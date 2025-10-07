print ("===== Calculate Grade Program =====")

S = []
G = []

n = 1

while True :
    name = input(f"Enter student name No.{n:.0f} : ")
    grade = float(input("Enter Grade : "))

    S.append(name)
    G.append(grade)

    c = input("Continue? (y/n) : ")
    if c == "n":
        break
    n += 1
print ()
print ("===== Report =====")
Average = sum(G)/len(G)
Maxgrade_index = G.index(max(G))
Mingrade_index = G.index(min(G))

print (f"Average : {Average:.2f}")
print ("Max :",S[Maxgrade_index])
print ("Min :",S[Mingrade_index])