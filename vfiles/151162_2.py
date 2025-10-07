v1 = input("Enter v1 (space-speparated): ")
v2 = input("Enter v2 (space-speparated): ")
v3 = input("Enter v3 (space-speparated): ")
v4 = input("Enter v4 (space-speparated): ")
v5 = input("Enter v5 (space-speparated): ")
v6 = input("Enter v6 (space-speparated): ")

v1 = int(v1)
v2 = int(v2)
v3 = int(v3)
v4 = int(v4)
v5 = int(v5)
v6 = int(v6)

v_list = [v1, v2, v3]
v_list2 = [v4, v5, v6]

dot_product = v1*v4+v2*v5+v3*v6
print(f"Dot product: {dot_product:.2f}")