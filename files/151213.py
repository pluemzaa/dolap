def dot(a,b):
  if len(a) != len(b):
    return 0
  else:
    return sum([x[0]*x[1] for x in zip(a,b)])
  
in1 = input("Enter v1 (space-separated): ").split(' ')
in2 = input("Enter v2 (space-separated): ").split(' ')


in1 = [int(x) for x in in1]
in2 = [int(x) for x in in2]


# print(in1)
# print(in2)
print(f"Dot product: {dot(in1,in2)}")