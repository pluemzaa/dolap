h_in = int(input())
m_in = int(input())

h_out = int(input())
m_out = int(input())


start = h_in * 60 + m_in
end = h_out * 60 + m_out

if start < 7 * 60:
    start = 7 * 60
if end > 23 * 60:
    end = 23 * 60

time = end - start

if time <= 15:
    pay = 0
else:
    hour = (time + 59) // 60   
    if hour <= 3:
        pay = hour * 10
    elif hour <= 6:
        pay = (3 * 10) + ((hour - 3) * 20)
    else:
        pay = 200

print("Pay:" + str(pay))