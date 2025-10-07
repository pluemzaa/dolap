m = int(input("Enter number of sticks: "))
k = int(input("Enter meatballs per stick: "))
n = int(input("Enter meatballs per bag: "))
total_meatballs = m * k
if total_meatballs % n == 0:
    bags_needed = total_meatballs // n
else:
    bags_needed = total_meatballs // n + 1
print("Number of bags needed:", bags_needed)