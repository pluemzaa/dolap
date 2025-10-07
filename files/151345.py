animals = ['Dog', 'Cat', 'Fish']
pets = input("Enter your pets: ").split(',')
pets = list(map(str.strip, pets))
codes = [str(animals.index(pet)) for pet in pets]
print("Code of your pets:", ','.join(codes))