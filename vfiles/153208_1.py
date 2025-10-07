# Create a dictionnary to store pet codes
pet_codes = {"Dog":"0","cat":"1""Fish":"2"}

# Get input from the user pet_intput = input ("Enter your pet:")
#split the input into a list (',')
# Create a list to stose the codes code_list =[]
# Convert each pet name to its code for pet in pet_list:
 code = pet_codes[pet]
 code_list.append(code)
# show the result
print("code of your pets:",",".join(code_list))