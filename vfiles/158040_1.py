= int(input())
m_in = int(input())
h_out = int(input())
m_out = int(input())
time_in = h_in * 60 + m_in
time_out = h_out * 60 + m_out
totalmin = time_out - time_in

if total_min <= 15:
    fee = 0
else:
    hours = math.ceil(total_min / 60)

    if hours <= 3:
        fee = hours * 10
    else:
        if hours <= 6:
            fee = 3 * 10 + (hours - 3) * 20
        else:
            fee = 200