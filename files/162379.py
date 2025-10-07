def Euclidean(P:list,Q:list):
    return pow(sum([pow((x[0]-x[1]),2) for x in zip(P,Q)]),1/2)

data = []
label = []
while True:
    dataIn = input("Enter data example (x1,x2,x3 ...): ")
    if dataIn == 'exit':
        break
    dataIn = list(map(int,dataIn.split(',')))
    labelIn = input("Enter data example (y): ")
    data.append(dataIn)
    label.append(labelIn)
preDataIn = list(map(int,input("Prediction, enter your input (x1,x2,x3 ...): ").split(',')))
label_predict = None
dist = None
for data in zip(label,data):
    if(dist == None):
        dist = Euclidean(preDataIn,data[1])
        label_predict = data[0]
    elif Euclidean(preDataIn,data[1]) < dist:
        label_predict = data[0]
        dist = Euclidean(preDataIn,data[1])
print(f"Min Euclidean distance: {dist:.2f}")
print(f"Result : {label_predict}")