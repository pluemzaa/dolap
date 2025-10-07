num = input("Enter a series of numbers separated by commas: ")
n = num.split(",")

n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])
n4 = int(n[3])
n5 = int(n[4])

lek = [n1,n2,n3,n4,n5]
max_numbers = max(lek)

print(n1, "is the maximum value:", n1 == max_numbers)
print(n2, "is the maximum value:", n2 == max_numbers)
print(n3, "is the maximum value:", n3 == max_numbers)
print(n4, "is the maximum value:", n4 == max_numbers)
print(n5, "is the maximum value:", n5 == max_numbers)