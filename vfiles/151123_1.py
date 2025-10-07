name = input('Enter your name:Pongsathon')
_email = input('Enter your email: pongsathon@kku.ac.th')
_gpa = input('Enter your GPA: 4.00')

name = int(name)
_email = int(_email)
_gpa = float(_gpa)
data_list = [name,_email, _gpa]
data_tuple = (name,_email, _gpa)

data_dict = {"name": name, "_gmail": _gmail, "_gpa": _gpa}
print(data_list)
print(data_tuple)
print(data_dict)