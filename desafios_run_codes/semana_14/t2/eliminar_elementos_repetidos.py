def main():
    numeros = []

    for i in range(20):
        n = int(input())

        numeros.append(n)

    lista_sem_elementos_repetidos = []
    
    for n in numeros:
        if n not in lista_sem_elementos_repetidos:
            lista_sem_elementos_repetidos.append(n)
    
    print(lista_sem_elementos_repetidos)

if __name__ == "__main__":
    main()