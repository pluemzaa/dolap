x = input("").split(",")
a = int(x[0])
b = int(x[1])
z = [(a+b),(a-b),(a*b),(a/b),(a//b),(a%b),(a**b)]
print(f'{a}+{b}=',z[0],"\n"f'{a}-{b}=',z[1],"\n"f'{a}*{b}=',z[2],"\n"f'{a}/{b}=',z[3],"\n"f'{a}//{b}=',z[4],"\n"f'{a}%{b}=',z[5],"\n"f'{a}**{b}=',z[6])