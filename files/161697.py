data = []
label = []
while True:
    nums = input('Enter coordinates of point P (p1, p2,...,qn): ')
    if nums=='exit':
        break
    nums = nums.split(',')
    nums = [float(x) for x in nums]
    data.append(nums)
    lab = input('Enter coordinates of point Q (q1, q2,..., qn):')
    label.append(lab)    
print(data)
print(label)