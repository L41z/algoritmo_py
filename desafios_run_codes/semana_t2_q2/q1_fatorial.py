def main():
    n = int(input())
    print(fatorial(n))

def fatorial(num):
    if num == 0:
        return 1
    else:
        for i in range(num - 1, 0, -1):
            num *= i
        return num
    
if __name__ == "__main__":
    main()