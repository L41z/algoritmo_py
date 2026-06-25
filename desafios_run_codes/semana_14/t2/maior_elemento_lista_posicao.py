def main():
    numeros = []
    index = 0
    for _ in range(10):
        n = int(input())

        numeros.append((n, index))
        index += 1
    
    lista_sem_index = []
    maior = 0
    posicao_maior = 0
    for numero in numeros:
        if numero[0] > maior:
            maior = numero[0]
            posicao_maior = numero[1]
        lista_sem_index.append(numero[0])
        
    print(lista_sem_index)
    print(maior)
    print(posicao_maior)

if __name__ == "__main__":
    main()        