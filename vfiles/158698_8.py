ih = int(input())
im = int(input())
oh = int(input())
om = int(input())
ihim = ((ih*60)-420) + im
ohom = ((oh*60)-420) + om
mp = ohom-ihim 
if mp <= 15:
    print('Pay:0')
    #121
elif mp > 15 and mp <= 180:
    tt= -(-mp//60)*10
    print('Pay:{}'.format(tt))
elif mp > 180 and mp <= 360:
    tt= (-(-mp//60)*20)-30
    print('Pay:{}'.format(tt))
else:
    print("Pay:200")