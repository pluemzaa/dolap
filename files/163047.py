import math
wood = int(input())
ball = int(input())
pack = int(input())

allball = wood * ball

total = allball / pack

print(math.ceil(total))