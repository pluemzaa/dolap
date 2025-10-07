number = int(input("ต้องการสูตรคูณแม่ไหน? :"))
for i in range(1,6):
    result = number*i
    print("%d x %d = %d"%(number,i,result))