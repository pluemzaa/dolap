hour_in=int(input())
in_min=int(input())
hour_out=int(input())
out_min=int(input())
m_in_sum=hour_in*60+in_min
m_out_sum=hour_out*60+out_min
sum_inout=m_out_sum-m_in_sum

if sum_inout<=15:
    print("Pay:0")
elif sum_inout>15 and sum_inout<=180:
    if sum_inout<=61:
        print("Pay:10")
    elif sum_inout>=61:
        print(f"Pay:{10*2}")
    elif sum_inout>=121:
        print(f"Pay:{10*3}")
    elif sum_inout>=180:
        print(f"Pay:{10*3}")
elif sum_inout>=181 and sum_inout<=360:
    if sum_inout<241:
        print("Pay:50")
    elif sum_inout>241:
        print("Pay:50")
    elif sum_inout>=301:
        print(f"Pay:{20*2+30}")
    elif sum_inout>=360:
        print(f"Pay:{20*3+30}")
elif sum_inout>=360:
    print("Pay:200")