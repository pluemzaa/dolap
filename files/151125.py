n = input("Enter your name:")
e = input("Enter your email:")
g = input("Enter your GPA:")
g = float(g)
data_list = [n,e,g]
data_tuple = (n,e,g)
data_dict = {'name': n, 'email': e, 'GPA': g}
print(data_list)
print(data_tuple)
print(data_dict)