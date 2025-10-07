i=0
j=0
k=0
l=0
sum=0
name = []
grade = []

print ('===== Calculate Grade Program =====')
while True :
    i=i+1
    name_input = str(input('Enter student name No.{} : '.format(i)))
    name.append(name_input)
    grade_input = float(input('Enter Grade : '))
    grade.append(grade_input)
    sum = sum + grade[j]
    j=j+1
    con = str(input('Continue? (y/n) : '))
    if con == ('y'):
        continue
    elif con == ('n') :
        break

_max = grade[0]
for i in range (len(grade)) :
    if grade[i] > _max :
        _max = grade[i]
        k=k+1

_min = grade[0]
for i in range (len(grade)) :
    if grade[i] < _min :
        _min = grade[i]
        l=l+1

avg = sum/len(grade)
print ()
print("===== Report =====")
print ('Average : %.2f'%avg)
print('Max : ',name[k])
print('Min : ',name[l])