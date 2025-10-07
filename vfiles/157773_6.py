hours_in=int(input(""))
minutes_in=int(input(""))
hours_out=int(input(""))
minutes_out=int(input(""))
hours_result=hours_out - hours_in
minutes_result=minutes_out - minutes_in
Pay= 0
if minutes_result <= 15 and hours_result== 0:
     print("Pay:{}".format(Pay))
elif 0 <= hours_result <= 3:
  if minutes_result > o and hours_result < 3:
    hours_result +=1
  elif minutes_result == 0 and hours_result == 3:
    Pay = hours_result*10
    if minutes_result > 0 and hours_result >= 3:
      Pay += 20
      print("Pay:{}".format(Pay))
elif hours_result == 6 and minutes_result > 0:
  Pay +=200
  print("Pay:{}".format(Pay))