start = [ 0 , 1 ]
Date = ''
start_n = start[0] + start[1]
N = int(input('Enter the number of terms: '))
out = '0 1'

for n in range(2,N):
	
	start_n = start[n-1] + start[n-2]
	start.append(start_n)

for x in range(0,N):
	Date += str(start[x])
	Date += str(' ')
	
print(Date)