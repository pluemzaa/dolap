skw = int(input())
bps = int(input())
bpb = int(input()) 

ttl = skw * bps

if ttl % bpb == 0 :
    nb = ttl//bpb
else :
    nb = (ttl//bpb) + 1

print (nb)