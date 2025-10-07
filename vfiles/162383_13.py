data = []
label = []
predict = []
while True:
    nums = input('Enter data example (x1,x2,x3 ...): ')
    if nums=='exit':
        break
    nums = nums.split(',')   
    nums = [float(x) for x in nums]
    data.append(nums)
    lab = input('Enter data example (y): ')
    label.append(lab)
predict = input('Prediction, enter your input (x1,x2,x3 ...): ')
predict = predict.split(',')
predict = [float(x) for x in predict] 
dis = []  
for i in range(len(label)):
    v1 = data[i]
    s = 0
    for j in range(len(v1)):
        s += abs(v1[j] - predict[j])**2
        d = s**0.5
    dis.append(d)
min_dis = min(dis)
min_index = dis.index(min_dis)
print(f"Min Euclidean distance: {d:.2f}")
print("Result : ",label[min_index])