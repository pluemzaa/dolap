import math

def calculate_distance():
    """
    Calculates the distance between two points based on user input.
    """
    print("Enter the x-coordinate of point 1: ", end="")
    x1 = float(input())

    print("Enter the y-coordinate of point 1: ", end="")
    y1 = float(input())

    print("Enter the x-coordinate of point 2: ", end="")
    x2 = float(input())

    print("Enter the y-coordinate of point 2: ", end="")
    y2 = float(input())

    # Calculate the distance using the distance formula
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Print the distance formatted to two decimal places
    print(f"The distance between the two points is: {distance:.2f}")

# Call the function to run the program
calculate_distance()