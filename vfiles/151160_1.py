pets = {"Dog": 0, "Cat": 1, "Fish": 2}
data = input("Enter your pets: ")
result = [pets[i.strip()] for i in data.split(",")]
print("Code of your pets:", ",".join(result))