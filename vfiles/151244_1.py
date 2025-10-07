data_dict = {"Dog":0,"Cat":1,"Fish":2}
string_in = input("Enter your pets: ").split(',')
print("Code of your pets: ",end = '')
for i,word in enumerate(string_in):
  if i!= len(string_in)-1:
    print(data_dict[word],end=',')
  else:
    print(data_dict[word])