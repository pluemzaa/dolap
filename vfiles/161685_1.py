data = []
mean = []
s = 0
while True :
    exam = input("Enter data example (x1,x2,x3 ...): ")
    if exam == "exit":
        break
    y = input("Enter data example (y):")
    exam = exam.split(",")
    exam = [float(i) for i in exam]
    data.append(exam)
    mean.append(y)
predic = input("Prediction, enter your input (x1,x2,x3 ...):").split(",")
predic = [float(i) for i in predic]
index = 0
predic_num = 500
for i in range (len(data)) :
    s = 0
    for j in range (len(data[i])) :
       s +=  (data[i][j] - predic[j])**2
    s = s**0.5
    if s < predic_num  :
        index = i
        predic_num = s
print(f"Min Euclidean distance: {predic_num:.2f}")
print(f"Result : {mean[index]}")