print("===== Calculate Grade Program =====")
sd = []
sdg = []
i=1
while True:
    sd_n = input(f"Enter student name No.{i} :")
    sd_g = float(input("Enter Grade :"))

    sd.append(sd_n)
    sdg.append(sd_g)

    con = input("Continue ? (y/n):").strip().lower()
    if con !="y":
        break
    i+=1
av = sum(sdg) / len(sdg)
max_index = sdg.index(max(sdg))
min_index = sdg.index(min(sdg))

print("\n===== Report =====")
print(f"Average : {av:.2f}")
print(f"Max : {sd[max_index]}")
print(f"Min : {sd[min_index]}")