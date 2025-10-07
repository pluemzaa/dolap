te_e={"Dog":0,"Cat":1,"Fish":2}
fee={"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
ttt=input("Enter your pets:")
ttt=ttt.split(',')
print('Code of your pets:',end=' ')
print(f"Code of your pets: {te_e[bee[0]]},{te_e[bee[1]]},{te_e[bee[2]]},{te_e[bee[3]]},{te_e[bee[4]]}")
print("One-hot vectors:",end='\n')
print(f"{fee[bee[0]]}\n{fee[bee[1]]}\n{fee[bee[2]]}\n{fee[bee[3]]}\n{fee[bee[4]]}")