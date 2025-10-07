name = input('enter Pongsathon')
gmail = input('enter  pongsathon@kku.ac.th')
gpa = input('enter 4.00')
name = str(name)
gmail = str(gmail)
gpa = float(gpa)

data_list = [name, gmail ,gpa]
data_tuple = (name, gmail ,gpa)

data_dict = {"name": name, "gmail": gmail , "gpa": "gpa"}
print(data_list)
print(data_tuple)
print(data_dict)
print(data_dict['str'])