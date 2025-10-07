n = input("Enter numbers separated by commas: ")
n = n.split(",")
nums = int(input("Enter number to search: "))
f = False
for i in range(0,len(n)):
  n[i] = int(n[i])

for i in range(0,len(n)):
  if nums == n[i]:
    print("Found",nums,"at index",i)
    f = True
if f == False:
  print("No",nums,"found.")