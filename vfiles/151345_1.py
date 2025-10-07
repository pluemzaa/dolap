animals = ['Dog', 'Cat', 'Fish']
pets = input("Enter your pets: ").split(',')
pets = list(map(str.strip, pets))
codes = [str(animals.index(pet)) for pet in pets]
print("Code of your pets:", ','.join(codes))
print("Error: Please enter only Dog, Cat, or Fish (5 items total).")