pet = input("Enter your pets: ")
pet = pet.split(',')
code = {
  'Dog':0,
  'Cat':1,
  'Fish':2
}
print(f"Code of your pets: {code[pet]}")