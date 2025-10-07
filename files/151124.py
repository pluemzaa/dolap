name = input('Enter your name:')
mail = input('Enter your email:')
gpa = input('Enter your GPA:')
gpa = float(gpa)
_list = [name, mail, gpa]
print(_list)
_tuple = (name, mail, gpa)
print(_tuple)
_dic = {"name": name,"email": mail,"GPA": gpa}
print(_dic)