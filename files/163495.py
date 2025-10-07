member = input("Membership (y/n) : ")
total = int(input("Total amount : "))

if member == "y" :
    if total >= 1000:
        print(f"Discount : {(total*0.2):.2f}")
        print(f"Final Amount to Pay : {( total-(total*0.2)):.2f}") 
    elif 500 <= total <= 999:
        print(f"Discount : {(total*0.1):.2f}")
        print(f"Final Amount to Pay : {( total-(total*0.1)):.2f}") 
    else:
        print(f"Discount : {(total*0):.2f}")
        print(f"Final Amount to Pay : {( total-(total*0)):.2f}") 
elif member == "n" :
    if total >= 1000:
        print(f"Discount : {(total*0.05):.2f}")
        print(f"Final Amount to Pay : {( total-(total*0.05)):.2f}") 
    else:
        print(f"Discount : {(total*0):.2f}")
        print(f"Final Amount to Pay : {( total-(total*0)):.2f}")