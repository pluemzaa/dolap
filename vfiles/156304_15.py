nums = input("Enter a series of numbers separated by commas:")
numbers = [int(num.strip()) for num in nums.split(',')]
maximum = max(numbers)
for num in numbers:
        print(f"{num} is the maximum value: {num == maximum}")