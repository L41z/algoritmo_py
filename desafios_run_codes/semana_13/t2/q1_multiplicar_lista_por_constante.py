def multiplicar_lista_por_constante(lista, constante):
    for i in range(len(lista)):
        lista[i] *= constante
    return lista


def main():
    lista = []

    while True:
        valor = int(input())

        if valor == 0:
            break

        lista.append(valor)

    constante = int(input())
    lista_mutada = multiplicar_lista_por_constante(lista, constante)

    print(lista_mutada)

if __name__ == "__main__":
    main()