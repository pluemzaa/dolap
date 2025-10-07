pet_text = input("Enter your pets: ")
pet = pet_text.split(',')
data = {'Dog': 0,'Cat': 1,'Fish': 2}
data1 = data[pet[0]]
data2 = data[pet[1]]
data3 = data[pet[2]]
data4 = data[pet[3]]
data5 = data[pet[4]]
print(f"Code of your pets: {data1},{data2},{data3},{data4},{data5}")