k1 = input("Enter a series of numbers separated by commas: ")
g2 = k1.split(",")

g2[0]= int(g2[0])
g2[1]= int(g2[1])
g2[2]= int(g2[2])
g2[3]= int(g2[3])
g2[4]= int(g2[4])
  
slop = (g2[0]-min(g2))/(max(g2)-min(g2))
slop1 = (g2[1]-min(g2))/(max(g2)-min(g2))
slop2 = (g2[2]-min(g2))/(max(g2)-min(g2))
slop3 = (g2[3]-min(g2))/(max(g2)-min(g2))
slop4 = (g2[4]-min(g2))/(max(g2)-min(g2))


print("Normalized values:")
print(f"{slop : .2f}")
print(f"{slop1 : .2f}")
print(f"{slop2 : .2f}")
print(f"{slop3 : .2f}")
print(f"{slop4 : .2f}")