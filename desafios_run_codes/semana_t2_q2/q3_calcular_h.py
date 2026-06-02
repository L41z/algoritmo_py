def main():
    # h = 1 + 1 /2 + 1 / 3 + ... + 1 / n
    n = int(input())

    h = 0
    for i in range(1, n + 1):
        h += 1 / i

    print(f"{h:.4f}")

if __name__ == "__main__":
    main()