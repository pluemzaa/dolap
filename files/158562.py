A = int(input())
B = int(input())
C = int(input())
D = int(input())

H_OUT = (C*60) + D
H_IN = (A*60) + B
Z = H_OUT - H_IN
if Z <= 15:
  X = 0
elif Z > 15 and Z <= 180:
  V = (Z//60)*10
  if Z % 60 != 0:
    Y = 10
  else:
    Y = 0
  X = V + Y
elif Z > 180 and Z < 360:
  V = (Z//60)*10
  if Z % 60 != 0:
    Y = 20
  else:
    Y = 0
  X = V + Y
elif Z >= 240 and Z <= 360:
  V = (Z//60)*20
  if Z % 60 != 0:
    Y = 20
  else:
    Y = 0
  X = V + Y
else:
    X = 200
print('Pay:',X)