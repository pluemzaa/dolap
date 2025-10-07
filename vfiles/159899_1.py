mes = input("Enter input: ")
a = len(mes)
sum = ""
for i in range(a-1, -1, -1):
    sum += mes[i]
print(sum)