m_ship = input("Membership (y/n) : ")
total = int(input("Total amount :"))
if m_ship == 'n' and total >= 1000:
    discount = total*0.05
    print(f"{discount:.2f}")
    final = total-discount
    print(f"Final Amount to Pay : {final:.2f}")
elif m_ship == 'y' and total >= 1000:
    discount = total*0.20
    print(f"{discount:.2f}")
    final = total-discount
    print(f"Final Amount to Pay : {final:.2f}")
elif m_ship == 'y' and total >= 500:
    discount = total*0.10
    print(f"{discount:.2f}")
    final = total-discount
    print(f"Final Amount to Pay : {final:.2f}")
else:
    discount = 0
    print(f"{discount:.2f}")
    final = total-discount
    print(f"Final Amount to Pay : {final:.2f}")