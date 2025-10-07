list_P = list(map(int,input("Enter coordinates of point P (p1, p2,...,qn): ").split(',')))
list_Q = list(map(int,input("Enter coordinates of point Q (q1, q2,..., qn): ").split(',')))

def Euclidean(P:list,Q:list):
    return pow(sum([pow((x[0]-x[1]),2) for x in zip(P,Q)]),1/2)

if len(list_P) == len(list_Q): 
    print(f"Euclidean distance between point P and point Q: {Euclidean(list_P,list_Q):.2f}")
else:
    print("Error: Vectors must have the same size")