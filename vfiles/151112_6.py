x = input('Enter your name:')
y = input('Enter your email:')
z = input('Enter your GPA:')
z = float(z)
data_list = [x, y, z]
data_tuple = (x , y , z)
data_dict = {'name' : x,  'email' : y , 'GPA' : z}
print(data_list)
print(data_tuple)
print(data_dict)