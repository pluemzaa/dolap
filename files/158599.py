h_in = int(input())    
m_in = int(input())    
h_out = int(input())   
m_out = int(input())    
minutes_in = h_in * 60 + m_in
minutes_out = h_out * 60 + m_out

if minutes_in < 420 or minutes_out > 1380 or minutes_out < minutes_in:
    print("Invalid time")
else:
    total_minutes = minutes_out - minutes_in

    if total_minutes <= 15:
        pay = 0
    elif total_minutes <= 180:
        hours = (total_minutes + 59) // 60
        pay = hours * 10
    elif total_minutes <= 360:
        hours = (total_minutes + 59) // 60 
        pay = 3 * 10 + (hours - 3) * 20
    else:
        pay = 200

    print(f"Pay:{pay}")