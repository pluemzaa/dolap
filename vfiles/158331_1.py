x_in = int(input())
y_in = int(input())
x_out = int(input())
y_out = int(input())

min_in = x_in * 60 + y_in
min_out = x_out * 60 + y_out

parking = min_out - min_in

if parking <= 15:
    pay = 0
elif parking <= 180:
    hours = (parking + 59) // 60
    pay = hours * 10
elif parking <= 360:
    hours = (parking + 59) // 60
    pay = 3 * 10
    ex_hours = hours - 3
    pay += ex_hours * 20
else:
    pay = 200

print("Pay:" + str(pay))