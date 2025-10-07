import math

# ฟังก์ชันคำนวณ Euclidean distance
def Euclidean(P: list, Q: list):
    return math.sqrt(sum((p - q) ** 2 for p, q in zip(P, Q)))

examples = []
labels = []

# รับข้อมูลจากผู้ใช้
while True:
    dataIn = input("Enter data example (x1,x2,x3 ...): ")
    if dataIn.strip().lower() == "exit":
        break

    feats = [float(n) for n in dataIn.split(",")]
    labelIn = input("Enter data example (y): ")

    examples.append(feats)
    labels.append(labelIn)

# รับข้อมูลที่จะใช้ทำนาย
preDataIn = [float(n) for n in input("Prediction, enter your input (x1,x2,x3 ...): ").split(",")]

label_predict = None
dist = None

# หา Euclidean distance ที่น้อยที่สุด
for label, example in zip(labels, examples):
    d = Euclidean(preDataIn, example)
    if dist is None or d < dist:
        dist = d
        label_predict = label

# แสดงผล
print(f"Min Euclidean distance: {dist:.2f}")
print(f"Result : {label_predict}")