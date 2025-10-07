def generate_one_hot_vectors_and_codes():
    """
    Prompts the user to enter 5 pet names separated by commas,
    then converts each name into its corresponding One-hot vector
    and also generates a 'Code of your pets' string.
    """

    # Define the mapping from pet names to One-hot vectors AND numerical codes
    pet_data = {
        "Dog": {"one_hot": [1, 0, 0], "code": 0},
        "Cat": {"one_hot": [0, 1, 0], "code": 1},
        "Fish": {"one_hot": [0, 0, 1], "code": 2}
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

            # Lists to store the generated codes and one-hot vectors
            pet_codes = []
            one_hot_vectors = []
            
            # Process each pet
            all_valid_pets = True
            for pet in pets:
                if pet in pet_data:
                    pet_codes.append(str(pet_data[pet]["code"]))
                    one_hot_vectors.append(pet_data[pet]["one_hot"])
                else:
                    print(f"Error: '{pet}' is not a recognized pet name. Please use Dog, Cat, or Fish.")
                    all_valid_pets = False
                    break # Stop processing if an invalid pet is found
            
            if not all_valid_pets:
                continue # Ask for input again if any pet was invalid

            # Print the results as per the example output format
            print(f"Enter your pets: {user_input}") # Echo user input
            print(f"Code of your pets: {','.join(pet_codes)}")
            print("One-hot vectors:")
            for vec in one_hot_vectors:
                print(vec)
            
            break # Exit the loop if input is valid and processed

        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

# Call the function to run the program
if __name__ == "__main__":
    generate_one_hot_vectors_and_codes()