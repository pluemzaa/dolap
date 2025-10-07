data_dict = {"Dog":"0","Cat":"1","Fish":"2"}
sain = input("Enter your pets:").split(",")
Code_list = [data_dict[pet] for pet in sain]
print("Code of your pets:",",".join(Code_list))