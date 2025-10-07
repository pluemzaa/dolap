pat = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
pat_n = input("Enter your pets:")
pat_nm = pat_n.split(",")
print("One-ot vectors:")
print(pat[pat_nm[0]])
print(pat[pat_nm[1]])
print(pat[pat_nm[2]])
print(pat[pat_nm[3]])
print(pat[pat_nm[4]])