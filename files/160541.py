nums = input("Enter numbers separated by commas: ")
n = [int(x) for x in nums.split(",")]
y = int(input("Enter number to search: "))
c = "at index"
d = "found."

found = False
for i in range(len(n)):
    if n[i] == y:
        print("Found", y, c, i)
        found = True

if not found:
    print("No", y, d)