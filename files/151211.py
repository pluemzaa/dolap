#Enter your name: Pongsathon
#Enter your email: pongsathon@kku.ac.th
#Enter your GPA: 4.00
#['Pongsathon', 'pongsathon@kku.ac.th', 4.0]
#('Pongsathon', 'pongsathon@kku.ac.th', 4.0)
#{'name': 'Pongsathon', 'email': 'pongsathon@kku.ac.th', 'GPA': 4.0}

name = input('Enter your name: ')
mail = input('Enter your email: ')
gpa = input('Enter your GPA: ')
gpa = float(gpa)

sec1 = [name,mail,gpa]
sec2 = (name,mail,gpa)
sec3 = {"name" : name ,"email" : mail, "GPA" : gpa}
print (sec1)
print (sec2)
print (sec3)