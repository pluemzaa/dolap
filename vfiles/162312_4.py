while True:
    p_input = input("Enter coordinates of point P (p1, p2, ..., pn) or 'exit' to quit: ")
    if p_input == "exit":
        break

    q_input = input("Enter coordinates of point Q (q1, q2, ..., qn) or 'exit' to quit: ")
    if q_input == "exit":
        break

    p = [float(x) for x in p_input.split(',')]
    q = [float(x) for x in q_input.split(',')]
    print("Error: Please enter only numeric values separated by commas.")
    
    if len(p) != len(q):
        print("Error: Vectors must have the same size")
    distance = sum((a - b)  2 for a, b in zip(p, q))  0.5
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")