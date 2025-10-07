def main():
    membership = input("Membership (y/n) : ").strip().lower()
    try:
        total = float(input("Total amount : ").strip())
    except ValueError:
        total = 0.0

    is_member = (membership == 'y')

    if is_member:
        if total >= 1000:
            rate = 0.20
        elif total >= 500:
            rate = 0.10
        else:
            rate = 0.0
    else:
        if total >= 1000:
            rate = 0.05
        else:
            rate = 0.0

    discount = total * rate
    final_amount = total - discount

    print(f"Discount : {discount:.2f}")
    print(f"Final Amount to Pay : {final_amount:.2f}")

if __name__ == "__main__":
    main()