n = input("Membership (y/n) : ").lower()
t = float(input("Total amount :"))

m = (n == "y")

d = 0
if m and t >= 1000:
    d = 0.20
elif m and 500 <= t <1000:
    d = 0.10
elif not m and t >= 1000:
    d =0.05

d_t = t*d
n_t = t - d_t


print(f"Discount :{d_t:.2f}")
print(f"Final Amount to Pay :{n_t:.2f}")