def main():
    lista = []

    while True:
        try:
            valor = int(input())
            lista.append(valor)
        except EOFError:
            break

    pares = [x for x in lista if x % 2 == 0]
    impares = [x for x in lista if x % 2 != 0]

    print(lista)
    print(pares)
    print(impares)

if __name__ == "__main__":
    main()