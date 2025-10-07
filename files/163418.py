a=input("Enter item 1 :")
aa=float(input("Enter weight 1 :"))

b=input("Enter item 2 :")
bb=float(input("Enter weight 2 :"))

c=input("Enter item 3 :")
cc=float(input("Enter weight 3 :"))

d=input("Enter item 4 :")
dd=float(input("Enter weight 4 :"))


print(f'{a}           {aa:.2f}')
print(f'{b}           {bb:.2f}')
print(f'{c}           {cc:.2f}')
print(f'{d}           {dd:.2f}')
print('---------------------------')
cal=[aa,bb,cc,dd]
total=sum(cal)
print(f'total           {total:.2f}')