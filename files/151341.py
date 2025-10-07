def get_vector(prompt):
    while True:
        try:
            v = list(map(int, input(prompt).strip().split()))
            if len(v) != 3:
                print("กรุณาป้อนตัวเลข 3 ตัว")
                continue
            return v
        except ValueError:
            print("กรุณาป้อนแต่ตัวเลข")

v1 = get_vector("Enter v1 (space-separated): ")
v2 = get_vector("Enter v2 (space-separated): ")

dot_product = sum([a*b for a, b in zip(v1, v2)])
print(f"Dot product: {dot_product}")