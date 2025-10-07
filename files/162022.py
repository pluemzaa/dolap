def main():
    try:
        n = int(input("Enter number: "))
    except ValueError:
        print("Error: invalid input")
        return

    if n < 1:
        print("Error number must be 1 or greater")
        return

    for i in range(1, n + 1):
        line = "*" * (2 * i)
        print(line)
        print(line)

if __name__ == "__main__":
    main()