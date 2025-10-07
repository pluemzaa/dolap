H_in = int(input())
M_in = int(input())
H_out = int(input())
M_out = int(input())

all_M_in = H_in * 60 + M_in
all_M_out = H_out * 60 + M_out
result = all_M_out - all_M_in

if result <= 15:
    print("Pay:0")
elif result <= 60:
    print("Pay:10")
elif result <= 120:
    print(f"Pay:{10*2}")
elif result <= 180:
    print(f"Pay:{10*3}")
elif result <= 240:
    print(f"Pay:{50}")
elif result <= 300:
    print(f"Pay:{20*2+30}")
elif result <= 360:
    print(f"Pay:{20*3+30}")
else:
    print("Pay:200")