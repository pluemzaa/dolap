correct_username = "admin"
correct_password = "password123"
count = 1
while count <= 3:
  a = input("Enter username: ")
  b = input("Enter password: ")
  if a != correct_username or b != correct_password:
    print("Invalid credentials. Try again.")
    count += 1
print("Maximum login attempts reached. Access denied.")