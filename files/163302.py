def main():
    member = input("Membership (y/n) : ").strip().lower()
    amount = float(input("Total amount : ").strip())

    if member == 'y':
        if amount >= 1000:
            rate = 0.20
        elif amount >= 500:
            rate = 0.10
        else:
            rate = 0.0
    else:
        if amount >= 1000:
            rate = 0.05
        else:
            rate = 0.0

    discount = amount * rate
    final_amount = amount - discount

    print(f"Discount : {discount:.2f}")
    print(f"Final Amount to Pay : {final_amount:.2f}")

if __name__ == "__main__":
    main()