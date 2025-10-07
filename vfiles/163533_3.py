print('===== Calculate Grade Program =====')
number = 1
av = 0
Max = []
while True :
    n = input(f"Enter student name No.{number} : ")
    g = float(input("Enter Grade : "))
    c = input("Continue? (y/n) : ")
    number += 1
    av += g
    _max = max
    Max.append(_max)
    _min = min
    if c == 'n' :
        break

print()
print("===== Report =====")
avg = av/(number-1)
print(f'Average : {avg:.2f}')
print(f'Max :{Max} ')
print(f'Min : ')