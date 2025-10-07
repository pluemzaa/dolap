def generate_one_hot_vectors():
    """
    Prompts the user to enter 5 pet names separated by commas,
    and then converts each name into its corresponding One-hot vector.
    """

    # Define the mapping from pet names to One-hot vectors
    pet_to_one_hot = {
        "Dog": [1, 0, 0],
        "Cat": [0, 1, 0],
        "Fish": [0, 0, 1]
    }

    while True:
        try:
            # Get input from the user
            user_input = input("Enter your pets (e.g., Dog,Cat,Dog,Fish,Cat): ")

            # Split the input string by commas and remove leading/trailing whitespace
            pets = [pet.strip() for pet in user_input.split(',')]

            # Check if exactly 5 pet names were entered
            if len(pets) != 5:
                print("Error: Please enter exactly 5 pet names, separated by commas.")
                continue # Ask for input again

            print("\nOne-hot vectors:")
            # Convert and print the One-hot vector for each pet
            for pet in pets:
                if pet in pet_to_one_hot:
                    print(pet_to_one_hot[pet])
                else:
                    # Handle cases where the pet name is not recognized
                    print(f"Warning: '{pet}' is not a recognized pet name. Skipping.")
            break # Exit the loop if input is valid and processed
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

# Call the function to run the program
if __name__ == "__main__":
    generate_one_hot_vectors()