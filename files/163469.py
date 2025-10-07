print('===== Calculate Grade Program =====')

i = 1
mini = [5, 'p']
maxi = [0, 'p']
total = 0
while True:
    name = input(f'Enter student name No.{i} : ')
    g = float(input('Enter Grade : '))
    
    if g < mini[0]:
        mini[0] = g
        mini[1] = name
    if g > maxi[0]:
        maxi[0] = g
        maxi[1] = name
        
    total += g
    if input('Continue? (y/n) : ') == 'n':
        break
    
    i += 1

print()
print('===== Report =====')
print('Average : %.2f' %(total / i))
print('Max :', maxi[1])
print('Min :', mini[1])