n1 = input("Enter your pets: ")
n5 = n1.split(",")
n_ = {"Dog": 0, "Cat": 1, "Fish": 2}

print("Code of your pets:", end=" ")
print(n_[n5[0].strip()],
      n_[n5[1].strip()],
      n_[n5[2].strip()],
      n_[n5[3].strip()],
      n_[n5[4].strip()], sep=",")