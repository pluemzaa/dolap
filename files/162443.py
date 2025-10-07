import math

def parse_vector(s):
    return [float(x.strip()) for x in s.split(',') if x.strip() != '']

p_str = input("Enter coordinates of point P (p1, p2,...,qn): ")
q_str = input("Enter coordinates of point Q (q1, q2,..., qn): ")

p = parse_vector(p_str)
q = parse_vector(q_str)

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    sum_sq = 0.0
    for pi, qi in zip(p, q):
        diff = qi - pi
        sum_sq += diff * diff

    d = math.sqrt(sum_sq)

    print(f"Euclidean distance between point P and point Q: {d:.2f}")