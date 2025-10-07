app=str(input('Enter item 1 : '))
appW=float(input('Enter weight 1 : '))
papa=str(input('Enter item 2 : '))
papaW=float(input('Enter weight 2 : '))
baba=str(input('Enter item 3 : '))
babaW=float(input('Enter weight 3 : '))
ora=str(input('Enter item 4 : '))
oraW=float(input('Enter weight 4 : '))

total=appW+papaW+babaW+oraW

print(f'{app}                   {appW:.2f}')
print(f'{papa}                   {papaW:.2f}')
print(f'{baba}                   {babaW:.2f}')
print(f'{ora}                   {oraW:.2f}')
print('---------------------------')
print(f'Total                     {total:.2f}')