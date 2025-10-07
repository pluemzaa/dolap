print("===== Calculate Grade Program =====")

grade_list = []
name_list = []
i = 0
while True:
    name = input(f'Enter student name No.{i+1} : ')
    name_list.append(name)
    grade = float(input('Enter Grade : '))
    grade_list.append(grade)
    c = input('Continue? (y/n) : ')
    i += 1
    if c == 'y':
        continue
    else:
        print()
        print('===== Report =====')
        avg = sum(grade_list) / len(grade_list)
        m_xname = max(zip(grade_list, name_list))
        m_nname = min(zip(grade_list, name_list))
        print(f'Average : {avg:.2f}')
        print(f'Max : {m_xname[1]}')
        print(f'Min : {m_nname[1]}')
        break