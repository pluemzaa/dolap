data_dict = {"Dog":0,"Cat":1,"Fish":2}
vector = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
sain = input("Enter your pets:").split(',')
print(f"Code of your pets: {data_dict[sain[0]]},{data_dict[sain[1]]},{data_dict[sain[2]]},{data_dict[sain[3]]},{data_dict[sain[4]]}")
print("One-hot vectors:")
print(f"{vector[sain[0]]}\n{vector[sain[1]]}\n{vector[sain[2]]}\n{vector[sain[3]]}\n{vector[sain[4]]}")