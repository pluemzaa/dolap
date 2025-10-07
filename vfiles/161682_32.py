from math import sqrt

def parse_vec(s: str):
    parts = [x.strip() for x in s.split(',') if x.strip() != ""]
    return [float(x) for x in parts]

print("Enter coordinates of point P (p1, p2,...,qn): ", end="")
p_raw = input()
print("Enter coordinates of point Q (q1, q2,..., qn): ", end="")
q_raw = input()

p = parse_vec(p_raw)
q = parse_vec(q_raw)

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    d = sqrt(sum((qi - pi) ** 2 for pi, qi in zip(p, q)))
    print(f"Euclidean distance between point P and point Q: {d:.2f}")