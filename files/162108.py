import math

def euclidean_distance(vector1, vector2):
    """
    Function to calculate Euclidean distance between two vectors.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same size")
    
    sum_of_squares = 0
    for i in range(len(vector1)):
        diff = vector1[i] - vector2[i]
        sum_of_squares += diff**2
    
    return math.sqrt(sum_of_squares)

training_data = []
while True:
    data_input = input("Enter data example (x1,x2,x3 ...): ")
    if data_input.lower() == 'exit':
        break
    
    label_input = input("Enter data example (y): ")
    
    try:
        features = [float(x) for x in data_input.split(',')]
        training_data.append({'features': features, 'label': label_input})
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        continue

if not training_data:
    print("No training data provided. Exiting program.")
else:
    try:
        predict_input_str = input("Prediction, enter your input (x1,x2,x3 ...): ")
        predict_features = [float(x) for x in predict_input_str.split(',')]
    except ValueError:
        print("Invalid input for prediction. Please enter numbers separated by commas.")
        exit()

    min_distance = float('inf')
    closest_label = None

    for example in training_data:
        try:
            distance = euclidean_distance(predict_features, example['features'])
            if distance < min_distance:
                min_distance = distance
                closest_label = example['label']
        except ValueError as e:
            print(f"Skipping example due to dimension mismatch: {e}")
            continue

    if closest_label:
        print(f"Min Euclidean distance: {min_distance:.2f}")
        print(f"Result : {closest_label}")
    else:
        print("Could not make a prediction. Check your input and training data.")