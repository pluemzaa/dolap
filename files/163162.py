# input :

# ===== Calculate Grade Program =====
# Enter student name No.1 : Ake
# Enter Grade : 4.00
# Continue? (y/n) : y
# Enter student name No.2 : Boy
# Enter Grade : 3.50
# Continue? (y/n) : y
# Enter student name No.3 : Joey
# Enter Grade : 3.00
# Continue? (y/n) : n

 

# output :

# ===== Report =====
# Average : 3.50
# Max : Ake
# Min : Joey
# enter  menu (1=coke,2=pepsi):1
# you selec coke
# continue ?(y/n):y
# enter  menu (1=coke,2=pepsi):1
# you selec coke
# continue ?(y/n):y
# enter  menu (1=coke,2=pepsi):2
# you selec pepsi
# # continue ?(y/n):n
# your order:
# coke 2 25
# pepsi 1 20
print("===== Calculate Grade Program =====")
menu = int(input("enter  menu (1=coke,2=pepsi):"))
cp = 0
cc = 0
pp =0
pc = 0
while True:
    menu
    if menu ==1:
        print("you selec coke")
        cp = cp + 25
        cc = cc+1
    elif menu == 2:
        print("you selec pepsi")
        pp = pp+20
        pc = pc+1
    else :
        print("invald item")
        
    cont = input("Continue? (y/n) :")
    if cont=="n":
        break
print('===== Report =====')
print("Average :",cc,cp)
print("Max :",pc,pp)
print("Min :",pc,pp)