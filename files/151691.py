dataa_dict = {"Dog":0,"Cat":1,"Fish":2}
datae = {"Dog":[1, 0, 0],"Cat":[0, 1, 0],"Fish":[0, 0, 1]}
sain = input("Enter your pets: ").split(',')
print(f"Code of your pets: {dataa_dict[sain[0]]},{dataa_dict[sain[1]]},{dataa_dict[sain[2]]},{dataa_dict[sain[3]]},{dataa_dict[sain[4]]}")
print("One-hot vectors:")
print(f"{datae[sain[0]]}\n{datae[sain[1]]}\n{datae[sain[2]]}\n{datae[sain[3]]}\n{datae[sain[4]]}")