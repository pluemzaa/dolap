na1 = input("Enter your name:")
em1 = input("Enter your email:")
ga1 = input("Enter your GPA:")

ga1 = float(ga1)

data_list = [na1,em1,ga1]
data_tuple = (na1,em1,ga1)
data_dict = {"name":na1,"email":em1,"GPA":ga1}
 
print(data_list)
print(data_tuple)
print(data_dict)