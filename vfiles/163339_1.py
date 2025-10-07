print('===== Calculate Grade Program =====')
i=1
i=i+1

p1 = input('Enter student name No.1:')
g1 = float(input("Enter Grade :"))
c = input("Continue? (y/n) :")
if c == "y":
    p2 = input('Enter student name No.2 :')
    g2 = float(input("Enter Grade :"))
    c = input("Continue? (y/n) :")
    p3 = input('Enter student name No.3 :')
    g3 = float(input("Enter Grade :"))
    c = input("Continue? (y/n) :")
    a = (g1+g2+g3)/3
if c=='n':
    print()
    print('===== Report =====')
    print(f'Average :{a:.2f}')
    print('Max:' ,p1)
    print('Min:' ,p3)