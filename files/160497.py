n1 = input("Enter numbers separatedby commas:")
n1 =n1.split(",")

s1 = int(input("Enter number to search:"))

for i in range(0,len(n1)):
    n1[i] = int(n1[i])

for i in range(0,len(n1)):
    if s1 == n1[i]:
        print(F"Found {s1} at index",i)
else :
    print(F"No {s1} found.")