N = int(input("Enter the number of terms: "))
run = [0,1]
for i in range(2, N):
  run.append(int(run[i-1]) + int(run[i-2]))
result = run[ :N]
print(result)