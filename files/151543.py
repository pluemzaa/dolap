hname = {"Dog":0,"Cat":1,"Fish":2}
pets = input("Enter your pets: ").split(",")
codes = [hname[pet.strip()] for pet in pets]
print("Code of your pets:", ",".join(map(str, codes)))