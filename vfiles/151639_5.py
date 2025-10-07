pat_codes = {"DOG": 0, "CAT": 1, "FISH": 2}
pat = input("Enter your pets: ").split(",")

print("Result:", end=" ")
print(pat_codes[pat[0]],
        pat_codes[pat[1]],
        pat_codes[pat[2]], 
        pat_codes[pat[3]],
        pat_codes[pat[4]], sep=' , ')