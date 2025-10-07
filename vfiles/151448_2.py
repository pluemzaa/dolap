name = input("Enter your name: ")
email=input("Enter your email: ")
GPA=float(input("Enter your GPA: ")
data_list =[name,email,GPA] 
data_tuple=(name,email,GPA)
data_dict={"name":name,"email":email,"GPA":GPA}
print(data_list,data_tuple,data_dict,sep="\n")