N=int(input("Enter a number N: "))
print(f"Prime numbers from 1 to {N} are:")
for num in range(2, N + 1):
    x = 0
    for i in range(1, num + 1):
      if num % i == 0:
            x = x+1
    if x == 2:
        print(num)