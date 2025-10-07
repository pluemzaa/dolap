n = input().split(",")
n = [int(x.strip()) for x in n]

y = int(input())

found = False
for i in range(len(n)):
    if n[i] == y:
        print(f"Found {y} at index {i}")
        found = True

if not found:
    print(f"No {y} found")