from math import sqrt

X = []
Y = []

while True:
    data = input("Enter data example (x1,x2,x3 ...):")
    if data.lower() == 'exit':
        break
    feat = [float(i) for i in data.split(',')]
    lable = input("Enter data example (y): ")
    
    X.append(feat)
    Y.append(lable)
    
    feat_input = input("Prediction, enter your input (x1,x2,x3 ...):")
    feat_input = [float(i) for i in feat_input.split(",")]
    min_dis = None
    min_lable = None
    
    for i in range(len(X)):
        dis = sqrt(sum((feat_input[j] - X[i][j]) ** 2 for j in range(len(feat_input))))
        
        if(min_dis is None) or (dis < min_dis):
            min_dis = dis
            min_lable = Y[i]
    
    print(f"Min Euclidean distance: {min_dis:.2f}")
    print(f"Result: {min_lable}")