num1 = input('Enter a series of numbers separated by commas:')
num2 = num1.split(',')

num2[0] = int(num2[0])
num2[1] = int(num2[1])
num2[2] = int(num2[2])
num2[3] = int(num2[3])
num2[4] = int(num2[4])

num_max = max(num2)

print(num2[0],'is the maximum value:', num2[0] == num_max )
print(num2[1],'is the maximum value:', num2[1] == num_max )
print(num2[2],'is the maximum value:', num2[2] == num_max )
print(num2[3],'is the maximum value:', num2[3] == num_max )
print(num2[4],'is the maximum value:', num2[4] == num_max )