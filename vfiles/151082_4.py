name = input('Enter your name: ')
gmail = input('Enter your email: ')
gpa = input('Enter your GPA: ')
name = str(name)
gmail = str(gmail)
gpa = float(gpa)

data_list = [name, gmail ,gpa]
data_tuple = (name, gmail ,gpa)

data_dict = {"name": name, "gmail": gmail , "gpa": gpa}
print(data_list)
print(data_tuple)
print(data_dict)