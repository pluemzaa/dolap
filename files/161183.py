a_list = []
b_list = []
n_list = []
n = 0
total = 0

while True:
      a = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
      b = float(input("Please enter the number of parking hours: "))
      if a == 1:
        if b >= 1:
          n = 10 + 5 * (b-1)
          print("Parking fee: %.2f" %n,'THB')
          total += n
          n_list.append(n)
        elif b < 1 and b >= 0:
          n = 0
          print("Parking fee: 00.00 THB")
          total += n
          n_list.append(n)
        else:
          print("Please enter a valid number of parking hours")
          total += n
          n_list.append(n)
      elif a == 2:
        if b >= 1:
          n = 30 + 15 * (b-1)
          print("Parking fee: %.2f" %n,'THB')
          total += n
          n_list.append(n)
        elif b < 1 and b >= 0:
          n = 0
          print("Parking fee: 00.00 THB")
          total += n
          n_list.append(n)
        else:
          print("Please enter a valid number of parking hours")
          total += n
          n_list.append(n)
      else:
        print("Invalid vehicle type")



      if (a==1 or a ==2) and b > 0:
         a_list.append(a)
         b_list.append(b)

      con = input("Do you want to continue? (y/n): ")
      print('------------------------------')

      if con != "y":
        break

x = len(a_list)
print('VT Hours Cost')
for i in range(x):
    print(a_list[i],'%.2f'%b_list[i],'%.2f'%n_list[i])

print('Total %.2f '%total,'THB')