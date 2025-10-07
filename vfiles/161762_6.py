X = []
y = []

while True:
    x_input_str = input("Enter data example (x1,x2,x3 ...): ")
    if x_input_str.lower() == 'exit':
        break
    
    x_input_list = [int(x) for x in x_input_str.split(',')]
    y_label = input("Enter data example (y): ")
    
    X.append(x_input_list)
    y.append(y_label)

prediction_input_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
prediction_input = [int(x) for x in prediction_input_str.split(',')]

if len(prediction_input) != len(X[0]):
    print(f"Error: Prediction vector must have the same size as example vectors ({len(X[0])}).")
else:
    min_distance = -1
    predicted_label = ""
    
    for i in range(len(X)):
        squared_diff_sum = 0
        for j in range(len(X[i])):
            squared_diff_sum = squared_diff_sum + (X[i][j] - prediction_input[j])**2
        
        distance = squared_diff_sum**0.5
        
        if min_distance == -1 or distance < min_distance:
            min_distance = distance
            predicted_label = y[i]
    
    print(f"Min Euclidean distance: {min_distance:.2f}")
    print(f"Result : {predicted_label}")