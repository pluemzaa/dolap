en = (input("Enter numbers separated by commas: "))
en = en.split(",")
i = 0
ens = int(input('Enter number to search: ')) 
for i in range(0,len(en)):
    en[i] = int(en[i])
for i in range(0,len(en)):
    if ens == en[i]:
        print(f"Found {ens} at index {i}")

             
print(f"No {ens} found.")