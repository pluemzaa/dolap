name = input('enter yourname: ')
email= input('enter your email: ')
GPA = input('enter your GPA:')
GPA =float(GPA)
_list = [name,email,GPA]
_tuple = (name,email,GPA)
_dict = {
    'name':name,
    'email':email,
    'GPA': GPA
}
print(_list)
print(_tuple)
print(_dict)