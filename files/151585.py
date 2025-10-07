Pet = {'Dog':0 ,'Cat':1, 'Fish':2}
EP = input('Enter your pets:')
EP = EP.split(',')
print('Code of your pets:', end= ' ')
print(Pet[EP[0]],Pet[EP[1]],Pet[EP[2]],Pet[EP[3]],Pet[EP[4]],sep=',')
print('One-hot vectors:')
NP = {'Dog':'[1,0,0]','Cat':'[0,1,0]','Fish':'[0,0,1]'}

print(NP[EP[0]])
print(NP[EP[1]])
print(NP[EP[2]])
print(NP[EP[3]])
print(NP[EP[4]])