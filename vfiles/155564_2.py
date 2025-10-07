x = (input("Enter a series of numbers separated by commas:"))
a = x.split(",")
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
a[3] = int(a[3])
a[4] = int(a[4])


max_n = (max(a))
#print(max_n)
print(f"10 is the maximum value:{a[0] is max_n}")
print(f"1 is the maximum value:{a[1] is max_n}")
print(f"5 is the maximum value:{a[2] is max_n}")
print(f"1 is the maximum value:{a[3] is max_n}")
print(f"7 is the maximum value:{a[4] is max_n}")
#10,1,5,1,7