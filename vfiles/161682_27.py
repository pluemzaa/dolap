import math

def main():
    p_input = input("Enter coordinates of point P (p1, p2,…,qn): ")
    q_input = input("Enter coordinates of point Q (q1, q2,…,qn): ")

    p = list(map(float, p_input.strip().split()))
    q = list(map(float, q_input.strip().split()))

    if len(p) != len(q):
        print("Error: Vectors must have the same size")
    else:
        d = 0
        for i in range(len(p)):
            d += (q[i] - p[i]) ** 2
        d = math.sqrt(d)
        print("Euclidean distance between point P and point Q: %.2f" % d)

if __name__ == "__main__":
    main()