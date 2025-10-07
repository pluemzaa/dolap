def main():
    items = []
    weights = []

    for i in range(1, 5):
        item = input(f"Enter item {i} : ")
        weight = float(input(f"Enter weight {i} : "))
        items.append(item)
        weights.append(weight)

    for it, w in zip(items, weights):
        print(f"{it:<10}{w:>10.2f}")
    print("-" * 30)
    print(f"{'total':<10}{sum(weights):>10.2f}")

if __name__ == "__main__":
    main()