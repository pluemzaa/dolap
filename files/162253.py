data1_str = input("Enter coordinates of point P (p1, p2,...,qn):")
in1_str = input("Enter coordinates of point Q (q1, q2,..., qn):")

data2 = [int(x) for x in data1_str.split(",")]
in2 = [int(x) for x in in1_str.split(",")]

if len(data2) != len(in2):
  print("Error: Vectors must have the same size")
else:
  sum_sq_diff = 0
  for i in range(len(data2)):
    diff = data2[i] - in2[i]
    sum_sq_diff += diff**2
  distance = sum_sq_diff**0.5
  print(f"Euclidean distance between point P and point Q: {distance:.2f}")