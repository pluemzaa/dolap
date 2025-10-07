x = input("Enter a series of numbers separated by commas:")

x = x.split(",")
for i in range(len(x)):
    x[i] = int(x[i]) 
    
print("Normalized values:")

for i in range(len(x)):
    sum = (x[i] - min(x)) / (max(x) - min(x))  
    print(f"{sum:.2f}")