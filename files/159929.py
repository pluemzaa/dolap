terms = int(input("Enter the number of terms: "))
first = 0
second = 1
count = 0
while count < terms:
    print(first, end=" ")
    next_term = first + second
    first = second
    second = next_term
    count += 1