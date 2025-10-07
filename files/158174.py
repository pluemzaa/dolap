h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

t = (h2*60 + m2) - (h1*60 + m1)

if t <= 15: p = 0
elif t <= 180: p = ((t+59)//60)*10
elif t <= 360: p = 30 + ((t-180+59)//60)*20
else: p = 200

print(f"Pay:{p}")