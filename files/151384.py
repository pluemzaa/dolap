pets = input("Enter your pets: ").split(",")
Dict = {"Dog": 0, "Cat": 1, "Fish": 2}

print("Code of your pets: ",",".join(str(Dict[i]) for i in pets))