number = int(input("Enter key"))
y = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
     8: 'i', 9: 'j', 10: 'k', 11: 'l',12: 'm', 13: 'n', 14: 'o',
     15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v',
     22: 'w',23: 'x', 24: 'y', 25: 'z'}
x = [7,4,11,11,14]
q = (x[0] + number) % 26
w = (x[1] + number) % 26
e = (x[2] + number) % 26
r = (x[3] + number) % 26
t = (x[4] + number) % 26
print("Cipher of hello is {}{}{}{}{}".format(y[q],y[w],y[e],y[r],y[t]))