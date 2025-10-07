ih = int(input())
im = int(input())
oh = int(input())
om = int(input())
ihim = ((ih*60)-420) + im
ohom = ((oh*60)-420) + om
mp = ohom-ihim 
if mp <= 15:
    print('Pay:0')
elif mp > 15 and mp <= 60:
    print('Pay:10')
elif mp > 60 and mp <= 120:
    print('Pay:20')
elif mp > 120 and mp <= 180:
    print('Pay:30')
elif mp > 180 and mp <= 240:
    print('Pay:50')
elif mp > 240 and mp <= 300:
    print('Pay:70')
elif mp > 300 and mp <= 360:
    print('Pay:90')
else:
    print("Pay:200")