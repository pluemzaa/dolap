p=int(input())#ชั่วโมง
a=int(input())#นาที
y=int(input())#ชั่วโมง
z=int(input())#นาที
g=((y*60)+z)-((p*60)+a)
if g<=15:
    print('Pay:0')
elif g<=180:
    print('Pay:',((g+59)//60)*10)
    g<=360
elif g<=360:
    C=(g-180)#เกิน3ชั่วโมง
    K=((C+59)//60)*20#เงินที่เกิน3ชั่วโมง
    M=(180/60)*10#เงินของ3ชั่วโมง
    sum=K+1
    print ('Pay:',sum)
else:
    print('Pay:200')