nums = int(input("Enter a series of numbers separated by commas: "))
lst = [int(x) for x in nums.split(',')]
m = max(lst)
results = [((x == m) and True or False) for x in lst]
for x, res in zip(lst, results):
print(f"{x} is the maximum value: {res}")