N = int(input('Enter a number N: '))
print(f'Prime numbers from 1 to {N} are:')
for x in range(1,N) :
	a = 0
	for i in range(1,x) :
		if x % i != 0 :
			a += 1
		if a == (x-2) :
			print(x)