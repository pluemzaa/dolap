import math

for i in range(len(label)):
    v = data[i]
    d = 0
    for j in range(len(v)):
        d += (float(v[j]) - float(feat[j])) ** 2
    d = math.sqrt(d)   # เอารากที่สอง
    print(i, 'diff=', d)
    if d < min_diff:
        min_diff = d
        min_index = i