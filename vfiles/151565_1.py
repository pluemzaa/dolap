Pet = {'Dog':0 ,'Cat':1, 'Fish':2}
EP = input('Enter your pets:')
EP = EP.split(',')
print(Pet[EP[0]],Pet[EP[1]],Pet[EP[2]],Pet[EP[3]],Pet[EP[4]],sep=',')