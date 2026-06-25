def main():
    lista_a = []
    lista_b = []

    for _ in range(20):
        n = int(input())

        lista_a.append(n)
    
    for _ in range(20):
        n = int(input())

        lista_b.append(n)

    lista_c = []

    for i in range(len(lista_a)):
            lista_c.insert(i, lista_a[i] + lista_b[i])

    print(lista_a)
    print(lista_b)
    print(lista_c)

if __name__ == "__main__":
    main()