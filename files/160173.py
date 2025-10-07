list = input("Enter a series of numbers separated by commas:")
list = list.split(",")

i = 0
max = list[0]

while i < len(list):
    if int(list[i]) > int(max):
        max = list[i]
        
        print(f"set the maximum value to {max}")
    
    i += 1
    
print(f"The maximum value is {max}")