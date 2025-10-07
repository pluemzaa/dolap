print("===== Calculate Grade Program =====")

# a1 = input("Enter student name No.1 : ")
# b1 = float(input("Enter Grade : "))
# c1 = input("Continue? (y/n) : ")
re = 0
s = 0
c = []
while True:          
    a1 = input("Enter student name No.1 : ")
    b1 = float(input("Enter Grade : "))
    re += b1
    s += 1
    c = c.append(b1)
    
          
    c1 = input("Continue? (y/n) : ")
    r = max(c)
    h = min(c)
    if r == max(c):
        MAX = a1
    if h == min(c):
        MIN = a1
    
    
        
    if c1 == "n":
        break
      
        

    
        
print("===== Report =====")
print(f"Average : {re/s}")
print(f"Max : {MAX}")
print(f"Min : {MIN}")