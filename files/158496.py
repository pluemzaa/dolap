h_in = int(input())
min_in = int(input())
h_out = int(input())
min_out = int(input())
time_in = (h_in * 60) + min_in
time_out = (h_out * 60) + min_out

park = time_out - time_in
time_park = (park + 59 ) // 60
if park <= 15 :
    print("pay:0")
elif park > 15 and park <= 180 :
    print("pay:",time_park*10)
elif park > 180 and park < 240 :
    print("pay:50")
elif park > 180 and park <= 360 :
    print("pay:",time_park*20)
elif park > 360 :
    print("pay:200")