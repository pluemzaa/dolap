import math

X=[]
y=[]

while True:
    x_input=input('Enter data example (x1,x2,x3): ')
    if x_input.lower() == 'exit':
        break
    try:
        x_vector = [float(i.strip()) for i in x_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        continue
    
    label = input("Enter data example (y): ")
    X.append(x_vector)
    y.append(label)
    
if not X:
    print("No data provided, Exiting...")
    exit()

x_predict_input = input("Prediction. enter your input (x1,x2,x3 ...): ")
try:
    x_predict = [float(i.strip()) for i in x_predict_input.split(",")]
except ValueError:
    print("Invalid Input, Please enter only numbers.")
    exit()
if any(len(x) != len(x_predict) for x in X):
    print("Error: All vectors must have the same size as the input.")
    exit()
    
min_distance = None
predicted_label = None

for i in range(len(X)):
    distance = math.sqrt(sum((X[i][j] - x_predict[j]) ** 2 for j in range (len(x_predict))))
    if (min_distance is None) or (distance < min_distance):
        min_distance = distance
        predicted_label = y[i]
        
print(f"Min Euclidean distance: {min_distance:.2f}")
print(f"Result : {predicted_label}")