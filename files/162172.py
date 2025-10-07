import math

def main():
    try:
        p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
        q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")
        
        p = [float(x.strip()) for x in p_input.split(',')]
        q = [float(x.strip()) for x in q_input.split(',')]
        
        if len(p) != len(q):
            print("Error: Vectors must have the same size")
            return
        
        distance = math.sqrt(sum((p[i] - q[i])**2 for i in range(len(p))))
        
        print(f"Euclidean distance between point P and point Q: {distance:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers separated by commas")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()