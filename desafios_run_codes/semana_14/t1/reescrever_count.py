def contar(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1

    return contador

def main():
    lista = []

    while True:
        n = int(input())

        if n > 0:
            lista.append(n)
        else:
            break
    
    valor = int(input())

    print(lista)
    print(valor)
    print(contar(lista, valor))

if __name__ == "__main__":
    main()