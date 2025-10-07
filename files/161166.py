password = input('Enter a password: ')
if len(password) > 8 and any(i.isupper() for i in password) and any(i.islower() for i in password) and any(i.isdigit() for i in password):
    print('Password is valid.')
while len(password) <= 8 or not any(i.isupper() for i in password) or not any(i.islower() for i in password) or not any(i.isdigit() for i in password):
    print('Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.')
    password = input('Enter a password: ')