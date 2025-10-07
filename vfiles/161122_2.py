_num=input("Enter a series of numbers separated by commas: ")
num=[]
for text_num in _num.split(","):
    num.append(float(text_num))
max=max(num)
min=min(num)
print("Normalized values:")
for i in num:
    if max == min:
        print("0.00")
    else:
        x=(num-min)/(max-min)
        print(f"{x:.2f}")