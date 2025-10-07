ho = int(input())*60
mi = int(input())
outho = int(input())*60
outmi = int(input())

sum1 = (outho - ho) + (outmi - mi)

if sum1 <= 15:
    pay = 0
    print(f"Pay:{pay}")
    
elif sum1 >= 15 and sum1 <= 180:
    sum2 = ((sum1 + 59)//60) * 10
    print(f"Pay:{sum2}")

elif sum1 >= 180 and sum1 <= 360:
    sum3 = ((sum1 + 59)//60) * 20 - ((180+59)//60) * 10
    print(f"Pay:{sum3}")
else:
    OP = 200
    print(f"Pay:{OP}")