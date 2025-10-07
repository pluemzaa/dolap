C = {'Dog': '0', 'Cat': '1', 'Fish': '2'}
pets = input("Enter your pets: ").split(',')
codes = [C[pet] for pet in pets]
print("Code of your pets: " + ','.join(codes))