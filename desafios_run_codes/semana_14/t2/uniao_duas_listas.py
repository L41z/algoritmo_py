def main():
    lista_a = []
    lista_b = []

    for _ in range(10):
        n = int(input())

        lista_a.append(n)

    for _ in range(10):
        n = int(input())

        lista_b.append(n)

    lista_uniao = []
    for i in range(10):
        if lista_a[i] not in lista_uniao:
            lista_uniao.append(lista_a[i])
    for i in range(10):
        if lista_b[i] not in lista_uniao:
            lista_uniao.append(lista_b[i])
    print(lista_uniao)

if __name__ == "__main__":
    main()