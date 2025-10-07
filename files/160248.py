numbers = input("Enter a series of numbers separated by commas: ")
num_list = [int(x.strip()) for x in numbers.split(",")]

maximum = num_list[0]
i = 1  # เริ่มเทียบจากตัวที่สอง (index 1)

while i < len(num_list):
    if num_list[i] > maximum:
        maximum = num_list[i]
        print(f"set the maximum value to {maximum}")
    i += 1

print(f"The maximum value is {maximum}")