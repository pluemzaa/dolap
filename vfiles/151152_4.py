pet = input("Enter your pets: ")
pet = pet.split(',')
code = {
  'Dog': 0,
  'Cat': 1,
  'Fish': 2
}
code1 = code[pet[0]]
code2 = code[pet[1]]
code3 = code[pet[2]]
code4 = code[pet[3]]
code5 = code[pet[4]]
code_result = code1+code2+code3+code4+code5
print(f"Code of your pets: {code_result}")