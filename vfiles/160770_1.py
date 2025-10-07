def main():
    numbers = []
    
    while True:
        num = int(input("Enter a number (enter 0 to stop): "))
        if num == 0:
            break
        numbers.append(num)  
    
    if len(numbers) == 0:
        print("No numbers entered.")
    else:
        avg = sum(numbers) / len(numbers)  
        print("Average:", avg)

main()