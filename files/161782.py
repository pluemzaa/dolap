def print_number_square(n):
    if n < 1:
        print("Error number must be 1 or greater")
    else:
        for row in range(n):
            start = row + 1
            for col in range(n):
                value = (start + col - 1) % 9 + 1
                print(value, end=' ')
            print()

try:
    number = int(input("Enter number: "))
    print_number_square(number)
except ValueError:
    print("Error: invalid input. Please enter an integer.")