import math

p_input = input("Enter coordinates of point P (p1, p2,...,pn): ")
q_input = input("Enter coordinates of point Q (q1, q2,...,qn): ")

p = p_input.split(',')
q = q_input.split(',')

p_numbers = []
for item in p:
    item = item.strip()
    if item.lstrip('-').replace('.', '', 1).isdigit():
        p_numbers.append(float(item))
    else:
        print("Error: Please enter numbers only, separated by commas.")
        exit()

q_numbers = []
for item in q:
    item = item.strip()
    if item.lstrip('-').replace('.', '', 1).isdigit():
        q_numbers.append(float(item))
    else:
        print("Error: Please enter numbers only, separated by commas.")
        exit()

p = p_numbers
q = q_numbers

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    sum_squared = 0
    for i in range(len(p)):
        sum_squared += (p[i] - q[i]) ** 2
    distance = math.sqrt(sum_squared)

    print(f"Euclidean distance between point P and point Q: {distance:.2f}")