h_in = int(input())   
m_in = int(input())   
h_out = int(input()) 
m_out = int(input())  

start_minutes = h_in * 60 + m_in
end_minutes = h_out * 60 + m_out

duration = end_minutes - start_minutes

if duration % 60 == 0:
    hours = duration // 60
else:
    hours = (duration // 60) + 1

if duration <= 15:
    pay = 0
elif duration <= 180:  
    pay = hours * 10
elif duration <= 360:  
    if hours <= 3:
        pay = hours * 10
    else:
        first_part = 3 * 10
        second_part = (hours - 3) * 20
        pay = first_part + second_part
else:
    pay = 200  

print(f"Pay:{pay}")