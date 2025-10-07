data = []
lebal = []
while True:
    if len(nums) == len(lab):
            nums = input('Enter coordinates of point P (p1, p2,...,qn): ')
            if nums == 'exit':
                break
            nums = nums.split(',')
            nums = [float(x) for x in nums]
            data.append(nums)

    lab = input('Enter coordinates of point Q (q1, q2,..., qn): ')
    lebal.append(lab)

    else:
        print('Error: Vectors must have the same size')
print(data)
print(lebal)