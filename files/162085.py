import math

def euclidean_distance(vec1, vec2):
    distance = 0.0
    if len(vec1) != len(vec2):
        return float('inf')
    for i in range(len(vec1)):
        distance += (vec1[i] - vec2[i])**2
    return math.sqrt(distance)

def run_classifier():
    X_train = []
    y_train = []

    while True:
        x_input_str = input("Enter data example (x1,x2,x3 ...) : ")
        if x_input_str.lower() == 'exit':
            break

        y_input = input("Enter data example (y): ")

        try:
            x_coords = [float(coord) for coord in x_input_str.split(',')]
            X_train.append(x_coords)
            y_train.append(y_input)
        except ValueError:
            print("Invalid coordinate format. Please enter numbers separated by commas.")

    if not X_train:
        print("No data examples were entered.")
        return

    prediction_input_str = input(f"Prediction, enter your input (x1,x2,x3 ...) : ")

    try:
        prediction_vector = [float(coord) for coord in prediction_input_str.split(',')]
    except ValueError:
        print("Invalid prediction input format. Please enter numbers separated by commas.")
        return

    min_distance = float('inf')
    predicted_label = None

    for i in range(len(X_train)):
        distance = euclidean_distance(prediction_vector, X_train[i])
        if distance < min_distance:
            min_distance = distance
            predicted_label = y_train[i]

    if predicted_label is not None:
        print(f"Min Euclidean distance: {min_distance:.2f}")
        print(f"Result: {predicted_label}")
    else:
        print("Could not make a prediction. Ensure input dimensions match example dimensions.")

run_classifier()