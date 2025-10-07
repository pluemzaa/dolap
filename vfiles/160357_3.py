def min_max_normalize(data):
    """
    Normalizes a list of numbers to the range [0, 1] using Min-Max Normalization.

    Args:
        data: A list of numbers.

    Returns:
        A list of normalized numbers.
    """
    # Check for empty or single-element list to avoid division by zero
    if len(data) <= 1:
        # If there's one element, the result is 0. If empty, return empty.
        return [0.0] * len(data)

    min_val = min(data)
    max_val = max(data)
    
    # Check if max_val and min_val are the same to avoid division by zero
    if max_val == min_val:
        return [0.0] * len(data)

    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data

def main():
    """
    Main function to get user input, normalize the data, and print the results.
    """
    while True:
        try:
            user_input = input("Enter a series of numbers separated by commas: ")
            
            # Split the string by comma and convert each part to a float
            data = [float(x.strip()) for x in user_input.split(',')]
            
            # Normalize the data
            normalized_values = min_max_normalize(data)
            
            print("Normalized values:")
            for value in normalized_values:
                print(f"{value:.2f}") # Print with 2 decimal places
            
            break # Exit the loop if input is successful
            
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()