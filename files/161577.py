data = []
label = []

while True:
    x = input("Enter data example (x1,x2,x3 ...): ")
    
    if x == "exit":
        break
    
    x = [float(n) for n in x.split(",")]
    
    data.append(x)
    
    y = input("Enter data example (y): ")
    
    label.append(y)
    
xInput = input("Prediction, enter your input (x1,x2,x3 ...): ")
xInput = [float(n) for n in xInput.split(",")]

result = ""
minEuclidean = float("inf")

for i in range(len(data)):
    d = 0
    
    dataSample = data[i]
    
    for j in range(len(dataSample)):
        d += (dataSample[j] - xInput[j]) ** 2
        
    d **= 0.5
    
    if d < minEuclidean:
        minEuclidean = d
        
        result = label[i]
        
print(f"Min Euclidean distance: {minEuclidean:.2f}")
print(f"Result : {result}")