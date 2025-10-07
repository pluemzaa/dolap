hour_in = int(input())
minute_in = int(input())
hour_out = int(input())
minute_out = int(input())
total_in = hour_in * 60 + minute_in
total_out = hour_out * 60 + minute_out
total_hour = (total_out - total_in) //60
if total_out - total_in <= 15 :
    print("Pay:0")
else:
    if (total_out - total_in) %60 != 0:
        total_hour += 1 
    if total_hour <= 3 :
        total_pay = total_hour * 10
    elif total_hour <= 6 :
        total_pay = 3 * 10 + (total_hour - 3) * 20
    else :
        total_pay = 200
    print ("Pay:" , total_pay)