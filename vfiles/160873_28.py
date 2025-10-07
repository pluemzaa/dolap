a = 0
b = 0
fee = 0
hoa = 0
hob = 0
roa = 0
rob = 0
while True:

  car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
  ho = float(input("Please enter the number of parking hours: "))
  if car !=1 and car !=2 :
    print("Invalid vehicle type")
   
  elif ho <= 0 :
    print("Please enter a valid number of parking hours")
  else:
    if car == 1:
        if ho < 1 and ho > 0 :
            fee = 0
        elif ho >= 1 and ho < 2 :
            fee = 10
        elif ho >= 2 :
            fee = 10 + (ho - 1)*5
        print(f"Parking fee: {fee:.2f} THB")
        hoa += ho
        a += fee
        roa += 1
    
    if car ==2:
        if ho < 1 and ho > 0 :
            fee = 0
        elif ho >= 1 and ho < 2 :
            fee = 30
        elif ho >= 2 :
            fee = 30 + (ho - 1)*15
        print(f"Parking fee: {fee:.2f} THB") 
        hob += ho
        b += fee
        rob +=1        
         
  Continue = input("Do you want to continue? (y/n): ")
  print("------------------------------")
  if Continue.lower() == "n" :
      break
if roa >= 1 or rob >= 1 :
 print("VT Hours Cost")
 if roa >= 1 :
   print(f"1 {hoa:.2f} {a:.2f}")
 if rob >= 1 :
  print(f"2 {hob:.2f} {b:.2f}")
 total = a + b
 print(f"Total {total:.2f} THB")