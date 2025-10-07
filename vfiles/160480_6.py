i = input ("Enter numbers separated by commas: ")
s = int(input ("Enter number to search:"))

u = i.split(',')
i = [int(num)for num in  u]

found = False
for index, number in enumerate(i):
    if number==s:
        print(f"Found{s} at index {index}") 
        found = True
        
if not found:
    print(f"No {s}found.")