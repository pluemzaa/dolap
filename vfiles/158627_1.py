H_in=int(input())
M_in=int(input())
H_out=int(input())
M_out=int(input())

all_M_in=H_in*60+M_in
all_M_out=H_out*60+M_out
resalt=all_M_out-all_M_in

if resalt<=15 :
  print("Pay:0")
elif resalt>15 and resalt<=180:
    if resalt<61:
        print("Pay:10")
    elif resalt<=61 :
      print(f"Pay:{10*2}")
    elif resalt<=121 :
      print(f"Pay:{10*3}")
elif resalt>=181 and resalt<=360:
    if resalt>241 :
        print(f"Pay:{20*4}")
    elif resalt>=301 :
        print(f"Pay:{20*5}")
    elif resalt>=360 :
        print(f"Pay:{20*6}")
elif resalt>=360:
    print("Pay:200")