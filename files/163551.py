# item = []

# for i in range(4):
#     it = input(f"Enter item {i+1} :")
#     w = float(input(f"Enter weight {i+1} "))
    
#     item.append([it,w])
    
# total = 0
# for i in item:
#     print(f"{i[0]}        {i[1]:.2f}")
#     total += i[1] 
    
# print("---------------------------")
# print(f"total       {total:.2f}")    

#test2
# s1 = int(input())
# s2 = int(input())
# s3 = int(input())
# r = (s1*s2)/s3

# if r%1 == 0:
#     print(r)
# else:
#     r = ((s1*s2)//s3)+1
#     print(r)

#test3
# member = input("Membership (y/n) : ")
# total = int(input("Total amount : "))

# if member == "y" :
#     if total >= 1000:
#         print(f"Discount : {(total*0.2):.2f}")
#         print(f"Final Amount to Pay : {( total-(total*0.2)):.2f}") 
#     elif 500 <= total <= 999:
#         print(f"Discount : {(total*0.1):.2f}")
#         print(f"Final Amount to Pay : {( total-(total*0.1)):.2f}") 
#     else:
#         print(f"Discount : {(total*0):.2f}")
#         print(f"Final Amount to Pay : {( total-(total*0)):.2f}") 
# elif member == "n" :
#     if total >= 1000:
#         print(f"Discount : {(total*0.05):.2f}")
#         print(f"Final Amount to Pay : {( total-(total*0.05)):.2f}") 
#     else:
#         print(f"Discount : {(total*0):.2f}")
#         print(f"Final Amount to Pay : {( total-(total*0)):.2f}") 

#test4
print("===== Calculate Grade Program =====")
i = 1
sl = []
gl = []
while True:
    s = input(f"Enter student name No.{i} : ")
    g = float(input("Enter Grade : "))
    sl.append(s)
    gl.append(g)
    
    if input("Continue? (y/n) : ") == "n":
        break   

    i += 1
max_g = gl.index(max(gl))
min_g = gl.index(min(gl))
    
print()
print("===== Report =====")
print(f"Average : {(sum(gl)/len(gl)):.2f}")
print(f"Max : {sl[max_g]}")
print(f"Min : {sl[min_g]}")