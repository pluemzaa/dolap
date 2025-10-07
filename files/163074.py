num = int(input(""))
num2 = int(input(""))
num3 = int(input(""))
total = (num*num2)/num3
sum_ = (num*num2)%num3
if sum_ == 0:
    print(total)
else:
    total = total+1
    print(total)