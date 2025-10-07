pets = {"Dog": "1,0,0", "Cat": "0,1,0", "Fish": "0,0,1"}
data = input("Enter your pets: ")
result = [pets[i.strip()] for i in data.split(",")]
print("Code of your pets:", ",".join(result))