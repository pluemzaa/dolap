import math

vec1 = []
vec2 = []
sum = 0


vec1 = input("Enter coordinates of point P (p1, p2,...,qn): ").split(',')
vec1 = [float(x) for x in vec1]  

vec2 = input("Enter coordinates of point Q (q1, q2,..., qn): ").split(',')
vec2 = [float(x) for x in vec2]

if len(vec1) != len(vec2):
    print("Error: Vectors must have the same size")
else:
    for i in range(len(vec1)) : 
        y = 0
        y = (vec1[i] - vec2[i])**2
        sum = sum + y 

    sum = math.sqrt(sum)    

    print(f"Euclidean distance between point P and point Q:{sum:.2f}")