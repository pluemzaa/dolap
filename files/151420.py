pets = input("Enter your pets: ").split(",")
Dict = {"Dog": 0, "Cat": 1, "Fish": 2}
DictVector = {"Dog": [1, 0, 0], "Cat": [0, 1, 0], "Fish": [0, 0, 1]}

print("Code of your pets: ",",".join(str(Dict[i]) for i in pets))
print("One-hot vectors:")
print("\n".join(str(DictVector[i]) for i in pets))