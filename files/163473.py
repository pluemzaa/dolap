def calculate_discount(membership, total_amount):
    if membership == 'y':
        if total_amount >= 1000:
            return total_amount * 0.20
        elif total_amount >= 500:
            return total_amount * 0.10
    else:
        if total_amount >= 1000:
            return total_amount * 0.05
    return 0

def main():
    membership = input("Membership (y/n) : ").lower()
    total_amount = float(input("Total amount : "))
    discount = calculate_discount(membership, total_amount)
    final_amount = total_amount - discount
    print(f"Discount : {discount:.2f}")
    print(f"Final Amount to Pay : {final_amount:.2f}")

if __name__ == "__main__":
    main()