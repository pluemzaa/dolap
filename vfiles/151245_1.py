space1 = (input("Enter v1 (space-separated): ").split())
space2 = (input("Enter v2 (space-separated): ").split())
space_int1 = (int(space1))
space_int2 = (int(space2))
vector = [space_int1[0]]*[space_int2[0]]+[space_int1[1]]*[space_int2[1]]+[space_int1[2]]*[space_int2[2]]
print(space_int1,space_int2)