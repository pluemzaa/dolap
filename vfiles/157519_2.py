h_in=int(input())
m_in=int(input())
h_out=int(input())
m_out=int(input())
start = h_in * 60 + m_in
end = h_out * 60 + m_out
total_minutes = end - start
if total_minutes % 60 == 0:
    hours = total_minutes // 60
else:
    hours = (total_minutes // 60) + 1
if total_minutes <= 15:
    pay = 0
elif hours <= 3:
    pay = hours * 10
elif hours <= 6:
    pay = hours * 20
else:
    pay = 200
print("Pay:", pay)