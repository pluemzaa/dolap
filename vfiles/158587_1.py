hour_in=int(input())
in_min=int(input())
hour_out=int(input())
out_min=int(input())
m_in_sum=hour_in*60+in_min
m_out_sum=hour_out*60+out_min
sum_inout=m_out_sum-m_in_sum

if sum_inout<=15:
    print("pay:0")
elif sum_inout>15 and sun_inout<=180:
    if sum_inout<61:
        print("pay:10")
    elif sum_inout<=61:
        print(f"print:{10*2}")
    elif sum_inout<=121:
        print(f"pay:{10*3}")
    elif sum_inout<=180:
        print(f"pay:{10*3}")
elif sum_inout>=181 and sum_inout>=360:
    if sum_inout<241:
        print("pay:50")
    elif sum_inout>241:
        print("pay:50")
    elif sum_inout>=301:
        print(f"pay:{20*2+30}")
    elif sum_inout>=360:
        print(f"pay:{20*3+30}")
elif sum_inout>=360:
    print("pay:200")