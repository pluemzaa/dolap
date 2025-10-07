meat = int(input(""))
num = int(input(""))
sack = int(input(""))
s = (meat*num)
s_all = s/sack
if s % sack != 0:
    s_all += 1
print(int(s_all))