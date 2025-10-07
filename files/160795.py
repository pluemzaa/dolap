h_in = int(input())
m_in = int(input())
h_out = int(input())
m_out = int(input())

time_in = h_in * 60 + m_in
time_out = h_out * 60 + m_out
duration = time_out - time_in

if duration <= 15:
    pay = 0
elif duration <= 180:  
    hours = (duration + 59) // 60  
    pay = hours * 10
elif duration <= 360:  
    first_3_hr = 3 * 10
    remaining_time = duration - 180
    remaining_hours = (remaining_time + 59) // 60
    pay = first_3_hr + remaining_hours * 20
else:
    pay = 200

print(f"Pay:{pay}")