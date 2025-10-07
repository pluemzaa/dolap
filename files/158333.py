TimeIN_h = int(input())
TimeIN_m = int(input())
TimeOUT_h = int(input())
Timeout_m = int(input())
TimeINall = TimeIN_h*60+TimeIN_m
TimeOUTall = TimeOUT_h*60+Timeout_m
park = (TimeOUTall - TimeINall)
P = park
if P<=15:
    print("Pay:0")
else:
    hours = (P + 59) // 60
    if hours <= 3:
        print("Pay:",hours*10)
    elif hours <=6:
        print("Pay:",30+(hours - 3)*20)
    else:
        print("Pay:200")