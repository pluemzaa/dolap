import math

def main():
    p = list(map(float, input().split(',')))
    q = list(map(float, input().split(',')))

    if len(p) != len(q):
        print("Error: Vectors must have the same size")
    else:
        total = 0
        for i in range(len(p)):
            total += (q[i] - p[i]) ** 2
        d = math.sqrt(total)
        print("%.2f" % d)

if __name__ == "__main__":
    main()