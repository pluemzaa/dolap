a = {'Dog': 0, 'Cat': 1, 'Fish': 2}
b = {'Dog': [1, 0, 0], 'Cat': [0, 1, 0], 'Fish': [0, 0, 1]}

c = [x.strip() for x in input("Enter your pets: ").split(',')]

if len(c) != 5:
    exit()

try:
    d = [str(a[x]) for x in c]
    e = [b[x] for x in c]
except KeyError:
    exit()

print("Code of your pets:", ",".join(d))
print("One-hot vectors:")
for x in e:
    print(x)