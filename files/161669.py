import math
p = []
q = []
while True:
    nums = input("Enter coordinates of point P (p1, p2,...,qn): ")
    nums = nums.split(',')
    nums = [float(x) for x in nums]
    p.append(nums)
    

    lab = input("Enter coordinates of point Q (q1, q2,..., qn): ")
    lab = lab.split(',')
    lab = [float(x) for x in lab]
    q.append(lab)

    if len(p[-1]) != len(q[-1]):
        print("Error: Vectors must have the same size")
        p.pop() 
        q.pop() 
         

    sum_of_squares = 0
    for i in range(len(nums)):
        diff = nums[i] - lab[i]
        sum_of_squares += diff**2
    distance = math.sqrt(sum_of_squares)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")
    break