h_in=int(input(""))
m_in=int(input(""))
h_out=int(input(""))
m_out=int(input(""))
hours_total= h_out - h_in
minutes_total = m_out - m_in
pay = 0


if minutes_total <= 15 and hours_total == 0:
  print ("Pay:{}".format(pay))
elif 0  <= hours_total <= 3:
  if minutes_total > 0 and hours_total < 3:
    hours_total +=1
  elif minutes_total == 0 and hours_total == 3:
    pay = hours_total*10
  pay = hours_total*10
  if  minutes_total > 0 and hours_total >= 3:
    pay += 20
  print ("Pay:{}".format(pay))
elif hours_total == 6 and minutes_total > 0:
  pay += 200
  print("Pay:{}".format(pay))