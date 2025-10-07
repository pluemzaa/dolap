te_e = {"Dog":0,"Cat":1,"Fish":2}
fee = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
ttt = input("Enter your pets:")
ttt = ttt.split(',')
print ('Code of your pets:',end=' ')
print (te_e[ttt[0]],te_e[ttt[1]],te_e[ttt[2]],te_e[ttt[3]],te_e[ttt[4]],sep=',')
print ("One-hot vectors:",end='\n')
print (fee[ttt[0]],fee[ttt[1]],fee[ttt[2]],fee[ttt[3]],fee[ttt[4]],sep='\n')