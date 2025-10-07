print("===== Calculate Grade Program =====")

s = []
g = []

count = 1

while True:
    name = input(f"Enter student name No.{count} : ")
    geade = float(input("Enter Grade :"))

    s.append(name)
    g.append(geade)

    cout = input("Continue? (y/n) :")
    if cout == 'n':
        break

    count += 1

av = sum(g) / len(s)

max_geade_index = g.index(max(g))
min_geade_index = g.index(min(g))

print("\n===== Report =====")
print(f"Average : {av:.2f}")
print(f"Max : {max_geade_index:.2f}")
print(f"Min : {min_geade_index:.2f}")