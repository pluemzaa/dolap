inH=int(input("ชั่วโมงที่เข้า"))
inM=int(input("นาทีที่เข้า"))
outH=int(input("ชั่วโมงที่ออก"))
outM=int(input("นาทีที่ออก"))
i=((inH*60)+(inM))
out=(((outH*60)+(outM))-i)
h=((out+59)//60)
if (out <= 15) :
  print("Pay:",0)
elif (out > 15) and (out <= (3*60)) :
    print("Pay:",(h*10))
elif (out > (3*60)) and (out <= (6*60)) :
    print("Pay:",((h*20)-30))
elif (out > (6*60)) :
    print("Pay:",200)