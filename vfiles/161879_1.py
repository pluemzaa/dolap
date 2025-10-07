n = int(input("Enter number:"))
if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        for j in range(n):
            print(((i+j)%9)+1, end=' ')
        print()
        x = int(input('Enter number: '))
# row = col = x
# i = j = 1
# z = 1
# while i < row+1:
#     j = 0
#     while j < col:
#         if i + j > 100 :
#          z = 1      
#          print(z,end=' ')
#         else :
#             print(i+j,end=' ')    
#         j = j + 1
#     z = z + 1    
#     i = i + 1
#     print()