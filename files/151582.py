n1 = input("Enter your name:")
n2 = input("Enter your email:")
n3 = input("Enter your GPA:")

n3 = float(n3)
#list, tuple, set, dict
data_list = [n1, n2, n3]
data_tuple = (n1, n2, n3)
data_dict = {"name": n1, "email": n2, "GPA": n3}
print(data_list)
print(data_tuple)
print(data_dict)