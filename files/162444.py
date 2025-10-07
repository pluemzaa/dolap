import math

def euclidean_distance(point1, point2):
    
   
    distance = 0.0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i])**2
    return math.sqrt(distance)

def main():
    
    
    X_train = []
    y_train = []

    while True:
        x_input_str = input("Enter data example (x1,x2,x3 ...): ")
        
        if x_input_str.lower() == 'exit':
            break
            
        try:
            x_values = [float(val) for val in x_input_str.split(',')]
            
            y_value = input("Enter data example (y): ")
            
            X_train.append(x_values)
            y_train.append(y_value)
            
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas only.")

    if not X_train:
        print("\nNo training data provided. Exiting.")
        return

    while True:
        try:
            predict_input_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
            x_predict = [float(val) for val in predict_input_str.split(',')]
            
            if len(x_predict) != len(X_train[0]):
                print(f"Input dimension mismatch! Please enter {len(X_train[0])} features.")
                continue
            break
            
        except (ValueError, IndexError):
             print("Invalid input. Please enter numbers separated by commas.")

    min_dist = float('inf')
    best_label = None

    for i, x_example in enumerate(X_train):
        dist = euclidean_distance(x_predict, x_example)
        if dist < min_dist:
            min_dist = dist
            best_label = y_train[i]

    print(f"Min Euclidean distance: {min_dist:.2f}")
    print(f"Result: {best_label}")

if __name__ == "__main__":
    main()