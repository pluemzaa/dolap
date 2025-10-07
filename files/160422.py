num = input("Enter a series of numbers separated by commas: ").split(',')
num = [int(n) for n in num]
nummax = max(num)
nummin = min(num)
print("Normalized values:")
for n in range(0, len(num)):
    nums = (num[n] - nummin)/(nummax - nummin)
    n = n + 1
    print(f'{nums:.2f}')