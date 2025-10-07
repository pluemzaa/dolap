def Euclidean(P:list,Q:list):
    return pow(sum([pow((x[0]-x[1]),2) for x in zip(P,Q)]),1/2)

def Euclidean(P:list,Q:list):
    return pow(sum([pow((x[0]-x[1]),2) for x in zip(P,Q)]),1/2)

examples = []
labels = []
while True:
    dataIn = input("Enter data example (x1,x2,x3 ...): ")
    if dataIn == 'exit':
        break
    dataIn = list(map(int,dataIn.split(',')))
    labelIn = input("Enter data example (y): ")
    examples.append(dataIn)
    labels.append(labelIn)
    
preDataIn = list(map(int,input("Prediction, enter your input (x1,x2,x3 ...): ").split(',')))
label_predict = None
dist = None
for examples in zip(labels,examples):
    if(dist == None):
        dist = Euclidean(preDataIn,examples[1])
        label_predict = examples[0]
    elif Euclidean(preDataIn,examples[1]) < dist:
        label_predict = examples[0]
        dist = Euclidean(preDataIn,examples[1])

print(f"Min Euclidean distance: {dist:.2f}")
print(f"Result : {label_predict}")