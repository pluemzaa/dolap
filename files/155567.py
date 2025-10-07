x_num=input("Enter a series of numbers separated by commas:")
x=x_num.split(",")
x[0]=int(x[0])
x[1]=int(x[1])
x[2]=int(x[2])
x[3]=int(x[3])
x[4]=int(x[4])
r0=x[0]
r1=x[1]
r2=x[2]
r3=x[3]
r4=x[4]
_max=(max(x))
print(r0,"is the maximum value:",r0 == _max)
print(r1,"is the maximum value:",r1 == _max)
print(r2,"is the maximum value:",r2 == _max)
print(r3,"is the maximum value:",r3 == _max)
print(r4,"is the maximum value:",r4 == _max)