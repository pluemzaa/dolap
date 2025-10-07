pat = input("Enter your pets: ")
pat = pat.split(",")
pat_codes = {"DOG": 0, "CAT": 1, "FISH": 2}

print("Result:", end=" ")
print(pat_codes[pat[0]],
      pat_codes[pat[1]],
      pat_codes[pat[2]], sep=',')