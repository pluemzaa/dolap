k_dic = {"Dog":0,"Cat":1,"Fish":2}
name_str = input("Enter your pets:")
name = name_str.split(",")
print("Code of your pets:",end='')
print(k_dic[name[0]],
      k_dic[name[1]],
      k_dic[name[2]],
      k_dic[name[3]],
      k_dic[name[4]],sep=",")