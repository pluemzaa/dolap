message = input("")
number_list = message.split(",")

a = int(number_list[0].strip())
b = int(number_list[1].strip())
sum = a + b
print("sum is:", sum)