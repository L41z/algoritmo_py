def main():
    n = int(input())

    if is_prime(n):
        print("True")
    else:
        print("False")

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return n > 1

if __name__ == "__main__":
    main()