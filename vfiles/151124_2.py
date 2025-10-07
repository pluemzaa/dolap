name = input('Enter your name:')
mail = input('Enter your email:')
gpa = input('Enter your GPA:')
gpa = float(gpa)
_list = [name,mail,gpa]
_tuple = (name,mail,gpa)
_dic = {"name": name,"email": mail,"GPA": gpa}
print(_dic)
print(_list)
print(_tuple)