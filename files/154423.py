Num = input("")
Num_list = Num.split(',')
sum = int(Num_list[0]) + int(Num_list[1])
print (f"{Num_list[0]} + {Num_list[1]} = {sum}")

sum1 = int(Num_list[0]) - int(Num_list[1])
print (f"{Num_list[0]} - {Num_list[1]} = {sum1}")

sum2 = int(Num_list[0]) * int(Num_list[1])
print (f"{Num_list[0]} * {Num_list[1]} = {sum2}")

sum3 = int(Num_list[0]) / int(Num_list[1])
print (f"{Num_list[0]} / {Num_list[1]} = {sum3}")

sum4 = int(Num_list[0]) // int(Num_list[1])
print (f"{Num_list[0]} // {Num_list[1]} = {sum4}")

sum5 = int(Num_list[0]) % int(Num_list[1])
print (f"{Num_list[0]} % {Num_list[1]} = {sum5}")

sum6 = int(Num_list[0]) ** int(Num_list[1])
print (f"{Num_list[0]} ** {Num_list[1]} = {sum6}")