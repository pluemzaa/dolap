data_dict = {"Dog":0,"Cat":1,"Fish":2}
string_in = input("Enter your pets: ").split(',')
print("Code of your pets: ",end = '')

print(f"Code of your pets: {data_dict[string_in[0]]},{data_dict[string_in[1]]},{data_dict[string_in[2]]},{data_dict[string_in[3]]},{data_dict[string_in[4]]}")

# for i,word in enumerate(string_in):
#   if i!= len(string_in)-1:
#     print(data_dict[word],end=',')
#   else:
#     print(data_dict[word])