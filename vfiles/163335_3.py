print("===== Calculate Grade Program =====")

# a1 = input("Enter student name No.1 : ")
# b1 = float(input("Enter Grade : "))
# c1 = input("Continue? (y/n) : ")
a1 = 0
re = 0
s = 0
c = []
c1 = "y"
Max_ = None
Min_ = None
while True:
    if c1 == "y":      
        a1 = input("Enter student name No.1 : ")
        b1 = float(input("Enter Grade : "))
        re += b1
        s += 1
        if Max_ is None or b1 > Max_:
            MAX_ = b1
            MAX = a1
        if  Min_ is None or b1 < Min_:
            Min_ = b1
            MIN = a1  
        c1 = input("Continue? (y/n) : ")  
    elif c1 == "n":
        break   
print("===== Report =====")
print(f"Average : {re/s}")
print(f"Max : {MAX}")
print(f"Min : {MIN}")