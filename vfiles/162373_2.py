import math

def parse_coords(s):
    """รับสตริง เช่น '1, 2,3' หรือ '1 2 3' แล้วคืนเป็น list ของ float
       จะโยน ValueError หากไม่สามารถแปลงเป็นตัวเลขได้"""
    s = s.strip()
    if not s:
        raise ValueError("ไม่มีค่าที่ป้อนเข้ามา")
    # รองรับทั้ง comma และ space เป็นตัวคั่น
    s = s.replace(',', ' ')
    tokens = [t for t in s.split() if t != '']
    if not tokens:
        raise ValueError("ไม่พบตัวเลขในอินพุต")
    vals = []
    for t in tokens:
        try:
            vals.append(float(t))
        except ValueError:
            raise ValueError(f"ค่า '{t}' ไม่ใช่ตัวเลข")
    return vals

def euclidean_distance(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

# --- เก็บชุดข้อมูลตัวอย่าง (training examples) ---
X = []   # list of feature vectors (list of floats)
y = []   # labels/values (เก็บเป็น string เพื่อรองรับทั้งตัวเลขและข้อความ)

print("ป้อนข้อมูลตัวอย่างทีละตัว: รูปแบบ x1,x2,...,xn  (พิมพ์ 'exit' เพื่อจบการป้อน)")
while True:
    xin = input("Enter data example (x1,x2,...,xn) or 'exit': ").strip()
    if xin.lower() == 'exit':
        break
    try:
        xin_vals = parse_coords(xin)
    except ValueError as e:
        print("ผิดพลาดในการอ่าน feature:", e)
        continue

    yin = input("Label/value for this example (y): ").strip()
    if yin == '':
        print("กรุณาใส่ค่า y (ห้ามเว้นว่าง)")
        continue

    X.append(xin_vals)
    y.append(yin)
    print(f"เก็บตัวอย่างที่ {len(X)} ข้อมูลมิติ {len(xin_vals)} สำเร็จ\n")

if len(X) == 0:
    print("ไม่มีข้อมูลตัวอย่างให้ใช้คำนวณ — จบโปรแกรม")
    exit()

# --- รับ input ที่ต้องการทำ Prediction / หา nearest ---
while True:
    try:
        X_input_raw = input("Prediction: enter your input (x1,x2,...,xn): ").strip()
        X_input = parse_coords(X_input_raw)
        break
    except ValueError as e:
        print("ผิดพลาดในการอ่าน input:", e)

# หาเฉพาะตัวอย่างที่มีมิติเท่ากับ input
candidates = [(idx, sample) for idx, sample in enumerate(X) if len(sample) == len(X_input)]
if not candidates:
    print("ไม่พบตัวอย่างที่มีมิติเท่ากับ input ของคุณ")
    exit()

min_dist = None
min_index = -1
for idx, sample in candidates:
    d = euclidean_distance(sample, X_input)
    if (min_dist is None) or (d < min_dist):
        min_dist = d
        min_index = idx

print(f"\nNearest example index: {min_index+1} (0-based index: {min_index})")
print(f"Min Euclidean distance: {min_dist:.4f}")
print(f"Result (y): {y[min_index]}")