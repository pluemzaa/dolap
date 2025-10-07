pat = {"Dog":0,"cat":1,"fish":2}
pat_n = input("Enter your pets:")
pat_nm = pat_n.split(",")
print("Code of your pets:",end='')
print(pat[pat_nm[0]]),
pat[pat_nm[1]],
pat[pat_nm[2]],
pat[pat_nm[3]],
pat[pat_nm[4]],sep=',')