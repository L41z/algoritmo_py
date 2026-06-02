def main():
    x = int(input())
    y = int(input())

    for i in range(x, y + 1):
        if is_prime(i):
            print(i)

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return n > 1
    
if __name__ == "__main__":
    main()