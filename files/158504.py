h_in=int(input())
min_in=int(input())
h_out=int(input())
min_out=int(input())
h_inpas = h_in*60 + min_in
h_outpas =  h_out*60 + min_out
time = h_outpas - h_inpas
if time <= 15 :
    pay = 0
elif time <=180 :
    time2=time//60
    if  time%60 == 0:
     time2 += 0 
    else :
     time2 += 1 
    pay = time2 * 10
elif time<=360 :
    time3=time-180
    time3=time3//60
    if time%60 == 0 : 
        time3 += 0
    else :
     time3 +=1 
    pay = (time3 * 20) +30
else :
    pay= 200
print("Pay:",pay)