#  หากลูกค้าสั่งลูกชิ้น m ไม้ ซึ่งใน 1 ไม้มีลูกชิ้น k ลูก ถ้าลูกชิ้น 1 ถุงมี n ลูก นายเอต้องหยิบถุงลูกชิ้นมากี่ถุง ถึงจะพอขายให้ลูกค้าคนนั้น
# import math
m = float(input())
k = float(input())
n = float(input())
total = (m*k)
test = (total+n-1)//n
# print(test)
# total = math.ceil(total) 
print(int(test))