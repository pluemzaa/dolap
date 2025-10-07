prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
number = int(input("Enter a number: "))
if 0 <= number <= 100:
is_prime = number in prime_numbers
print("Is the number prime?", is_prime)
else:print("Number is out of range (0-100).")