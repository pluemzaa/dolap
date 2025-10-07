pat = {"Dog":0,"Cat":1,"Fish":2}
pat_n = input("Enter your pets:")
pat_nm = pat_n.split(",")
print("Code of your pets:",end='')
print(pat[pat_nm[0]],
pat[pat_nm[1]],
pat[pat_nm[2]],
pat[pat_nm[3]],
pat[pat_nm[4]],sep=',')

pets_codes = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
print("One-hot vectors:",end = '\n')
print(pat[pat_nm[0]],
pat[pat_nm[1]],
pat[pat_nm[2]],
pat[pat_nm[3]],
pat[pat_nm[4]],sep='\n')