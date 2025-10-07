data =[]
lable = []
brbr = []
while True:
    nums = input('Enter coordinates of point P (p1, p2,...,qn):')
    nums = nums.split(',')
    nums = [float(x) for x in nums]
    # add data
    data.append(nums)
    lab = input('Enter coordinates of point Q (q1, q2,..., qn):')
    lable.append(lab)