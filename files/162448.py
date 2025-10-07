import math

p_input = input("Enter coordinates of point P (p1, p2,...,qn):")
p_input = p_input.split(",")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn):")
q_input = q_input.split(",")

for i in range(len(p_input)):
    p_input[i] = int(p_input[i])
for i in range(len(q_input)):
    q_input[i] = int(q_input[i])
    
if len(p_input) != len(q_input):
    print("Error: Vectors must have the same size")
else:
    t = 0
    for i in range(len(p_input)):
        t += (q_input[i] - p_input[i])**2
        q = math.sqrt(t)
    print(f"Euclidean distance between point P and point Q: {q:.2f}")