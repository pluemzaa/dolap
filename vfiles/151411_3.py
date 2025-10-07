patt = {"Dog":0,"Cat":1,"Fish":2}
pat = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
pat_nm = input("Enter your pets:").split(",")
print(patt[pat_nm[0]],
patt[pat_nm[1]],
patt[pat_nm[2]],
patt[pat_nm[3]],
patt[pat_nm[4]],sep=',')
print("One-ot vectors:")
print(pat[pat_nm[0]])
print(pat[pat_nm[1]])
print(pat[pat_nm[2]])
print(pat[pat_nm[3]])
print(pat[pat_nm[4]])