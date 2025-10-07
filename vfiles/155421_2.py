nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

x = input("Enter a number:")
print("Is the number prime?")
print( x is nums)

PRIMES_0_100 = {
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97
}

n = int(input("Enter a number: "))

if 0 <= n <= 100:
    is_prime = n in PRIMES_0_100
    print("Is the number prime?", is_prime)
else:
    print("Out of range (0‑100)")