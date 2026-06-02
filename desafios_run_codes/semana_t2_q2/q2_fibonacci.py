def main():
    n = int(input())
    fib = fibonacci(n)

    print(str(fib)[1:-1])

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        fib = []
        a, b = 0, 1
        fib.append(a)
        fib.append(b)
        for i in range(2, num):
            a, b = b, a + b
            fib.append(b)
        return fib

if __name__ == "__main__":
    main()