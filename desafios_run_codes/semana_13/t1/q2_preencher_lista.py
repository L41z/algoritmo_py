def main():
    tam = int(input())
    lista = []

    # a) preencha com 0 (zero) e imprima a lista;
    for i in range(tam):
        n = 0
        lista.append(n)
    print(lista)

    # b) preencha com 1 a n e imprima a lista;
    lista = []
    for i in range(tam):
        n = i + 1
        lista.append(n)
    print(lista)


    #c) preencha com valores lidos pelo teclado e imprima a lista;
    lista = []
    for i in range(tam):
        n = int(input())
        lista.append(n)
    print(lista)

    #d) preencha na ordem inversa com valores lidos pelo teclado e imprima a lista;
    lista = []
    for i in range(tam):
        n = int(input())
        lista.insert(0, n)
    print(lista)


if __name__ == "__main__":
    main()