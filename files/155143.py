# Enter a number: 20
# Is the number prime? False


def isPrime(number):
    if number > 1:
        for i in range(number+1):
            if(i != number and i != 1 and i > 1):
                if(number % i == 0):
                   return False 
        return True
    else:
        return False
        
number = int(input("Enter a number: "))
print(f"Is the number prime? {isPrime(number)}")