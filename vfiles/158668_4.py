h_in = int(input())
m_in = int(input())
h_out = int(input())
m_out = int(input())
h_in = h_in*60
h_out = h_out*60

all_in = h_in+m_in
all_out = h_out+m_out

if(all_out - all_in) <= 15:
    print("pay:0")
elif(all_out - all_in) <= 60:
    print("pay:10")
elif(all_out - all_in) <= 180:
    print("pay:20")
elif(all_out - all_in) <= 360:
    print("pay:20")
else(all_out - all_in) > 360:
    print("pay:200")