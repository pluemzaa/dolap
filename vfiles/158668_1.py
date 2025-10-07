h_in = int(input())
m_in = int(input())
h_out = int(input())
m_out =  int(input())

all_in = (h_in*60) + m_in
all_out = (h_out*60) + m_out

time = (all_out - all_in)

if time <= 15:
    print("pay:0")
elif time <= 60 :
    print("pay:10")
elif time <= 180 :
    print("pay:30")
elif 181 < time <= 240 :
    print("pay:50")
elif time <= 360 :
    print("pay:50")
else:
    print("pay:200")