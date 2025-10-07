import math
x = []
y = []


while True:
    try:

        x_str = input("Enter data example (x1,x2,x3 ...): ")
        if x_str.lower() == 'exit':
            break
      
        features = [float(x) for x in x_str.split(',')]
        x.append(features)

       
        y_label = input("Enter data example (y): ")
        y.append(y_label)

    except (ValueError, IndexError):
        print("Invalid input. Please enter numbers separated by commas.")

try:
    X_input_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
    X_input = [float(x) for x in X_input_str.split(',')]


    min_dist = float('inf')  
    pred_class = ""


    for i in range(len(x)):
        current_x = x[i]
        sum_sq = 0


        for j in range(len(current_x)):
            diff = X_input[j] - current_x[j]
            sum_sq += diff ** 2
        

        distance = math.sqrt(sum_sq)


        if distance < min_dist:
            min_dist = distance
            pred_class = y[i]


    print(f"Min Euclidean distance: {min_dist:.2f}")
    print(f"Result: {pred_class}")

except (ValueError, IndexError):
    print("Invalid input for prediction. Please enter numbers separated by commas.")