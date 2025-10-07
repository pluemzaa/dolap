hours_in = int(input("A"))
minutes_in = int(input("C"))
hours_out = int(input("B"))
minutes_out = int(input("D"))
hrs_result = hours_out - hours_in
minutes_result = minutes_out - minutes_in
Pay = 0
if minutes_result <= 15 and hrs_result == 0:
    print("Pay:{}".format(Pay))
elif 0 <= hrs_result <= 3:
    if minutes_result > 0:
        hrs_result += 1
    Pay = (hrs_result*10)
    print("Pay:{}".format(Pay))
elif hrs_result == 6 and minutes_result > 0:
    Pay += 200
    print("Pay:{}".format(Pay))
elif 4 <= hrs_result <= 6:
    if minutes_result > 0 and 4 <= hrs_result <= 6:
        hrs_result +=1
    Pay = (hrs_result*20)
    print("Pay:{}".format(Pay))