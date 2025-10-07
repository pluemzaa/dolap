hi = int(input())
mi = int(input())
ho = int(input())
mo = int(intput())
kuy = hi * 60 + mi 
ryou = ho *60 + mo
non = ryou - kuy 
if  non <= 15  : 
  p = 0 
elif  non <= 180 :
  hou = non /60  
    if  non % 60 != 0 :
      hou +=1 
  p = hou * 10
elif non <= 360 :
   uou = non-180
     hou = uou/60
     if uou % 60 ! = 0 : 
       hon+=1 
   p =30 + uou * 20 
else :
 p = 200
print("Pay:",p)