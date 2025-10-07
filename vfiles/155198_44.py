number = input("Enter a series of numbers separated by commas: ")
numbers = [int(num) for num in number.split(",")]

max_number = max(numbers)
for num in numbers:
 print(f"{num} is the maximum number {max_number == num}")