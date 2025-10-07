input1=int(input("Enter key"))
Caesar = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',
8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',
17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
key1=Caesar[(7+(input1))%26]
key2=Caesar[(4+(input1))%26]
key3=Caesar[(11+(input1))%26]
key4=Caesar[(11+(input1))%26]
key5=Caesar[(14+(input1))%26]
print("Cipher of hello is",key1,key2,key3,key4,key5)