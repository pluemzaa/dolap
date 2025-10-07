num = input("Enter numbers separated by commas: ")
num = num.split(",")
num2 = int(input("Enter number to search: "))
i = 0
while i<len(num):
    num[i] = int(num[i])
    i+=1
i = 0
while i<len(num):
    if num2==num[i]:
        print("Found",num2,"at index",i,)    
    i=i+1 
i=0
while i<len(num):
    if num2!=num[i]:
        print("No",num2,"found.")
        break