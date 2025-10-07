mx = input("Enter v1 (space-separated): ")
my = input("Enter v2 (space-separated): ")

gex = mx.split(" ")
rex = my.split(" ")

gex[0] = int(gex[0])
gex[1] = int(gex[1])
gex[2] = int(gex[2])

rex[0] = int(rex[0])
rex[1] = int(rex[1])
rex[2] = int(rex[2])

num1 = gex[0] * rex[0]
num2 = gex[1] * rex[1]
num3 = gex[2] * rex[2]

numall = num1 + num2 + num3
print(f"Dot product: {numall}")