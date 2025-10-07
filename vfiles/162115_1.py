Feature = []
Label = []
while True:
    Pin = input("Enter data example (x1,x2,x3 ...): ")
    if Pin == "exit":
        break
    La = input('Enter data example (y): ')
    
    Pinv = Pin.split(",")
    Pinv = [float (x) for x in Pinv]
    Feature.append(Pinv)
    Label.append(La)
    
Qin = input("Prediction, enter your input (x1,x2,x3 ...): ")
Qinv = Qin.split(",")
Qinv = [float (x) for x in Qinv]

min_distance = float('inf')
min_index = -1

for i in range(len(Feature)):
    simple = Feature[i]
    d = sum((Qinv[j] - simple[j]) ** 2 for j in range(len(simple))) ** 0.5
    if d < min_distance:
            min_distance = d
            min_index = i

if min_index != -1:
    print(f"Min Euclidean distance: {min_distance:.2f}")
    print(f"Result : {Label[min_index]}")