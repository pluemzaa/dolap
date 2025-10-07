def print_square_pattern(n):
    if n < 1:
        print("Error number must be 1 or greater")
        return

    for row in range(1, n + 1):
        for col in range(1, n + 1):
            number = (row + col - 2) % 9 + 1
            print(number, end=" ")
        print()

try:
    n = int(input("Enter number: "))
    print_square_pattern(n)
except ValueError:
    print("Invalid input. Please enter an integer.")