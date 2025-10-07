menu = input("Enter item 1:")
p = float(input("Enter weight 1:"))
menu2 = input("Enter item 2:")
p2 = float(input("Enter weight 2:"))
menu3 = input("Enter item 3:")
p3 = float(input("Enter weight 3:"))
menu4 = input("Enter item 4:")
p4 = float(input("Enter weight 4:"))

print(f'{menu} {p: .2f}')
print(f'{menu2} {p2: .2f}')
print(f'{menu3} {p3: .2f}')
print(f'{menu4} {p4: .2f}')  

print('---------------------------')

pa = p+p2+p3+p4
print(f'total {pa: .2f}')