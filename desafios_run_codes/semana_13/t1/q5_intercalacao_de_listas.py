def main():
    A = []
    for _ in range(25):
        A.append(int(input()))

    B = []
    for _ in range(25):
        B.append(int(input()))

    C = []
    for i in range(25):
        C.append(A[i])
        C.append(B[i])

    print(A)
    print(B)
    print(C)

if __name__ == "__main__":
    main()