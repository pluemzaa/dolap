Hour_come = int(input("Hour of car is coming"))
Minute_come = int(input("Minute of car is coming"))
Hour_out = int(input("Hour of car is outing"))
Minute_out = int(input("Minute of car is outing"))
Sum1 = (Hour_out-Hour_come)*60
Sum2 = (Minute_out-Minute_come)
Sum1 = Sum1+Sum2
if Sum1 <= 15:
  print("Pay:0")
elif Sum1 <=180:
  print("Pay:" ,(Sum1//60)*10)
elif Sum1 <=360:
  print("Pay:" ,((Sum1//180)*20)+30)
else:
  print("Pay:200")