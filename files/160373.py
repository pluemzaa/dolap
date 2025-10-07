num = input("Enter a series of numbers separated by commas: ").split(',')
num = [int(n) for n in num]
maximum_ = num[0]
for i in range(0, len(num)):
    if maximum_ < num[i]:
        print("set the maximum value to", num[i])
        maximum_ = num[i]
        i += 1  
        continue    
print("The maximum value is ", maximum_)