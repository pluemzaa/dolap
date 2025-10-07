input_str = input("Enter a series of numbers separated by commas:")
numbers = [int(n)for n in input_str.split(',')]
max_value = max(numbres)
for num in numbers:
print(f"{num}is the maximum value:{num==max_value})