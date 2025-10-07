pat = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
pat_n = input("Enter your pets:")
pat_nm = pat_n.split(",")
print("One-ot vectors:")
print(pat[pat_nm[0]],sep=',')
print(pat[pat_nm[1]],sep=',')
print(pat[pat_nm[2]],sep=',')
print(pat[pat_nm[3]],sep=',')
print(pat[pat_nm[4]],sep=',')