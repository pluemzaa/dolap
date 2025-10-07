number = int(input("Enter a number N: "))
def is_prime(number):
  if number <= 1:
    return False
  for i in range(2, int(number**0.5)+1):
    if num % i == 0:
      return False
  return True
print("Prime numbers from 1 to", number,"are: ")
for num in range(1, number+1):
  if is_prime(num):
    print(num)