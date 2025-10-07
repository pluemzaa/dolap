def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum
    
h = int(input("Enter the number of rows for the pyramid: "))
box_total = sum(h)
print(f"The total number of boxes: {box_total}")
if box_total % 2 == 0:
    print("The total number of boxes is even")
    for i in range(1,h+1):
        print(str(i)*i)
else:
    print("The total number of boxes is odd")
    for i in range(0,h):
        print(str(h-i)*(h-i))