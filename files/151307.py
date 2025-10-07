#Enter v1 (space-separated): 1 2 3
#Enter v2 (space-separated): 4 5 6
#Dot product: 32
#Dot product ของ [1, 2, 3] และ [4, 5, 6] = 1 * 4 + 2 * 5 + 3 * 6 = 32

v1str = input("Enter v1 (space-separated): ")
v1 = v1str.split()
v2str = input("Enter v2 (space-separated): ")
v2 = v2str.split()

Z = list(map(int, v1))
X = list(map(int, v2))

r0 = Z[0] * X[0]
r1 = Z[1] * X[1]
r2 = Z[2] * X[2]

s = r0+r1+r2
print("Dot product:", s)