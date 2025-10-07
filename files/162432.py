import math

try:
    p_input_str = input("Enter coordinates of point P (p1, p2,...,qn):  ")
    p_str_list = p_input_str.split(',')

    q_input_str = input("Enter coordinates of point Q (q1, q2,..., qn): ")
    q_str_list = q_input_str.split(',')

    p = [float(coord) for coord in p_str_list]
    q = [float(coord) for coord in q_str_list]

   
    if len(p) != len(q):
        print("Error: Vectors must have the same size")
    else:
        sum_sq_diff = 0
        
        for i in range(len(p)):
            
            sum_sq_diff += (q[i] - p[i]) ** 2
        distance = math.sqrt(sum_sq_diff)
        
        
        print(f"Euclidean distance between point P and point Q: {distance:.2f}")

except ValueError:
   
    print("Error: Invalid input. Please enter only numbers separated by commas.")
except Exception as e:
   
    print(f"An unexpected error occurred: {e}")