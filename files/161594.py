n = int(input("Enter number: "))

if n < 1:
        print("Error number must be 1 or greater")
    
else:
    for i in range(1, n + 1):
        num_stars = i * 2
        star_line = '*' * num_stars
        print(star_line)
        print(star_line)