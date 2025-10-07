seofnum=input("Enter a series of numbers separated by commas:")
sfn=seofnum.split(",")
x0=int(sfn[0])
x1=int(sfn[1])
x2=int(sfn[2])
x3=int(sfn[3])
x4=int(sfn[4])
max_=max(x0,x1,x2,x3,x4)

xmax0=x0==max_
xmax1=x1==max_
xmax2=x2==max_
xmax3=x3==max_
xmax4=x4==max_
print(x0,"is the maximum value:",xmax0)
print(x1,"is the maximum value:",xmax1)
print(x2,"is the maximum value:",xmax2)
print(x3,"is the maximum value:",xmax3)
print(x4,"is the maximum value:",xmax4)