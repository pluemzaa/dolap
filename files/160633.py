nums = input("Enter a series of numbers separated by commas: ")
numbers = [int(x.strip()) for x in nums.split(",")]
if not numbers:
    print("No numbers entered.")
else:
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
            print(f"set the maximum value to {maximum}")

    print(f"The maximum value is {maximum}")