nums_text = input('Enter a series of numbers separated by commas:')
x = nums_text.split(",")
x[0] = int(x[0])
x[1] = int(x[1])
x[2] = int(x[2])
x[3] = int(x[3])
x[4] = int(x[4])



print(f"{x[0]} is the maximum value: {x[0] is max(x)}")
print(f"{x[1]} is the maximum value: {x[1] is max(x)}")
print(f"{x[2]} is the maximum value: {x[2] is max(x)}")
print(f"{x[3]} is the maximum value: {x[3] is max(x)}")
print(f"{x[4]} is the maximum value: {x[4] is max(x)}")