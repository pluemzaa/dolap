data=[]
label=[]
xinput=0
while True:
    
    xinput = input("Enter data example (x1,x2,x3 ...): ")
    if xinput =="exit":
        break
    xinput = xinput.split(',')
    xinput = [float(x)for x in xinput]
    data.append(xinput)

    y=input("Enter data example (y): ")
    label.append(y)
#print(data)
#print(label)

p=input("Prediction, enter your input (x1,x2,x3 ...): ")
p=p.split(',')
p=[float(x)for x in p]
min_diff=float('inf')
min_index=-1
for i in range(len(label)):
    v=data[i]
    d=0
    for j in range(len(v)):
        d+=(v[j]-p[j])**2
    d=d**0.5
    #print(i,'diff=',d)
    if d < min_diff:
        min_diff = d
        min_index = i
#print('min_index = ',i)
print(f"Min Euclidean distance: {min_diff:.2f}")
print("Result :",label[min_index])