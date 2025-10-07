pat_codes = {"Dog": 0, "Cat": 1, "Fish": 2}
pat = input("Enter your pets: ").split(",")
print("Code of your pets:", end=" ")
print(pat_codes[pat[0]],
pat_codes[pat[1]],
pat_codes[pat[2]], 
pat_codes[pat[3]],
pat_codes[pat[4]] , sep=' , ')

print("One-hot vectors:")
one_hot = {"0":  [1,0,0],  "1":  [0,1,0] , "2":  [0,0,1]}
print(one_hot[pat_codes[pat[0]]])
print(one_hot[pat_codes[pat[1]]])
print(one_hot[pat_codes[pat[2]]])
print(one_hot[pat_codes[pat[3]]])
print(one_hot[pat_codes[pat[4]]])