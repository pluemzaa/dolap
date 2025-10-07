print('===== Calculate Grade Program =====')
i = 1
n = []
g = []
while True:
    name = input(f'Enter student name No.{i} : ')
    grade = float(input('Enter Grade : '))
    n.append(name)
    g.append(grade)
    
    con = input('Continue? (y/n) : ')
    
    if con != 'y' :
        print()
        print('===== Report =====')
        print(f'Average : {sum(g)/len(g):.2f}')
        print('Max : ',min(n))
        print('Min : ',max(n))
        break
    
    i += 1