A = input("Enter a series of numbers separated by commas: ")

B = A.split(',')  

numbers = []
for text_number in B:
    num = float(text_number)  
    numbers.append(num)      

min_value = min(numbers)  
max_value = max(numbers)  

print("Normalized values:")

if max_value == min_value:
    print("cannot be calculated")
else:
    
    for x in numbers:
        
        normalized_result = (x - min_value) / (max_value - min_value)

        print(f"{normalized_result:.2f}")