input_str = input("Input: ")
numbers = input_str.split(",")
total = sum(int(num) for num in numbers)
print("sum is {total}")