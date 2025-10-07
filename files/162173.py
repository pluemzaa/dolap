import math

def main():
    X_train = []
    y_train = []
    
    while True:
        try:
            x_input = input("Enter data example (x1,x2,x3 ...): ")
            
            if x_input.lower() == 'exit':
                break
            
            x_features = [float(x.strip()) for x in x_input.split(',')]
            y_label = input("Enter data example (y): ")
            
            X_train.append(x_features)
            y_train.append(y_label)
            
        except ValueError:
            print("Error: Please enter valid numbers for features")
            continue
    
    if len(X_train) == 0:
        print("No training data provided")
        return
    
    try:
        prediction_input = input("Prediction, enter your input (x1,x2,x3 ...): ")
        X_input = [float(x.strip()) for x in prediction_input.split(',')]
        
        if len(X_input) != len(X_train[0]):
            print("Error: Input dimensions don't match training data dimensions")
            return
        
        distances = []
        for i in range(len(X_train)):
            distance = math.sqrt(sum((X_train[i][j] - X_input[j])**2 for j in range(len(X_input))))
            distances.append((distance, y_train[i]))
        
        min_distance, predicted_class = min(distances, key=lambda x: x[0])
        
        print(f"Min Euclidean distance: {min_distance:.2f}")
        print(f"Result : {predicted_class}")
        
    except ValueError:
        print("Error: Please enter valid numbers for prediction input")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()