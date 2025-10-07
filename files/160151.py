numbers = input("Enter numbers separated by commas:")
search = int(input("Enter number to search: "))

numbersL = numbers.split(",")

i = 0
c = 0

while i < len(numbersL):
    if int(numbersL[i]) == search:
        print(f"Found {search} at index {i}")
        
        c += 1
        
    i += 1
    
if c <= 0:
    print(f"No {search} found")