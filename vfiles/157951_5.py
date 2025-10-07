while True:
    password = input("Enter a password: ")

    # เงื่อนไขตรวจสอบความปลอดภัยของรหัสผ่าน
    is_long_enough = len(password) > 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if is_long_enough and has_upper and has_lower and has_digit:
        print("Password is valid.")
        break
    else:
        print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")