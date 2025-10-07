n = int(input("Enter number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    i = 1
    while i <= n:
        current_num = i
        j = 0
        while j < n:
            display_num = (current_num - 1) % 9 + 1
            print(display_num, end=" ")
            current_num += 1
            j += 1
        print()
        i += 1