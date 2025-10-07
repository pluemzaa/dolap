h_in = int(input())  
m_in = int(input())   
h_out = int(input())  
m_out = int(input()) 

in_minutes = h_in * 60 + m_in
out_minutes = h_out * 60 + m_out

total_minutes = out_minutes - in_minutes

if total_minutes <= 15:
    pay = 0
elif total_minutes <= 180: 
    hours = -(-total_minutes // 60) 
    pay = hours * 10
elif total_minutes <= 360:  
    hours = -(-total_minutes // 60)
    extra_hours = hours - 3
    pay = (3 * 10) + (extra_hours * 20)
else:
    pay = 200

print(f"Pay:{pay}")