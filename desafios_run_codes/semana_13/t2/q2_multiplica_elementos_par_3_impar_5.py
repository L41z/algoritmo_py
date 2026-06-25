def main():
    lista = []
    
    for _ in range(100):
        lista.append(int(input()))

    lista.sort()

    lista_modificada = []
    
    for i in range(len(lista)):
        if i % 2 == 0:
            lista_modificada.append(lista[i] * 3)
        else:
            lista_modificada.append(lista[i] * 5)

    print(lista_modificada)

if __name__ == "__main__":
    main()