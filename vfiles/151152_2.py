pet = input("Enter your pets: ")
pet = pet.split(',')
code = {
  'Dog': 0,
  'Cat': 1,
  'Fish': 2
}
code1 = code[pet[0].strip()]
code2 = code[pet[1].strip()]
code3 = code[pet[2].strip()]
code4 = code[pet[3].strip()]
code5 = code[pet[4].strip()]

print(f"Code of your pets: {code1},{code2},{code3},{code4},{code5}")