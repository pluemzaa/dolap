code = {"Dog": 0, "Cat": 1, "Fish": 2}
one_hot = {"Dog": [1, 0, 0], "Cat": [0, 1, 0], "Fish": [0, 0, 1]}

pets = input("Enter your pets: ").split(',')
pets = [p.strip() for p in pets[:5]]

code_list = [str(codes[p]) for p in pets]
print("Code of your pets: " + ",".join(code_list))

vectors = [one_hot[p] for p in pets]
for v in vectors:
    print(v)