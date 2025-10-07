def generate_number_matrix(n):
    for row in range(1, n + 1):
        for col in range(n):
            current_num = (row + col - 1) % 9 + 1
            print(current_num, end=" ")
        print()

def main():
    try:
        n_input = input("Enter number: ")
        n = int(n_input)

        if n < 1:
            print("Error number must be 1 or greater")
        else:
            generate_number_matrix(n)

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()