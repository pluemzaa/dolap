h_in = int(input())
m_in = int(input())
h_out = int(input())
m_out = int(input())
start = h_in * 60 + m_in
end = h_out * 60 + m_out
duration = end - start
if duration <= 15:
    pay = 0
else:
    hours = (duration + 59) // 60
    if hours <= 3:
        pay = hours * 10
    elif hours <= 6:
        pay = (3 * 10) + (hours - 3) * 20
    else:
        pay = 200

print(f"Pay:{pay}")