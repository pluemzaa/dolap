# Pattern n x n: numbers 1..9, wrap to 1 after 9
# Each row starts at its row index (1-based): row1 start=1, row2 start=2, ...

def main():
    try:
        n = int(input("Enter number: "))
    except ValueError:
        print("Error number must be 1 or greater")
        return

    if n < 1:
        print("Error number must be 1 or greater")
        return

    for i in range(1, n + 1):          # i = row number (1..n)
        row = []
        for j in range(n):              # j = 0..n-1 (column offset)
            val = ((i + j - 1) % 9) + 1 # wrap 1..9
            row.append(str(val))
        print(" ".join(row))

if __name__ == "__main__":
    main()