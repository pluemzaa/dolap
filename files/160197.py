a = input("Enter a series of numbers separated by commas:")
list = a.split(",")

i = 0

while i < len(list):
    list[i] = int(list[i])
    
    i += 1

min = min(list)
max = max(list)

i = 0

print("Normalized values:")

while i < len(list):
    x = list[i]
    
    print(f"{(x - min) / (max - min):.2f}")
   
    i += 1