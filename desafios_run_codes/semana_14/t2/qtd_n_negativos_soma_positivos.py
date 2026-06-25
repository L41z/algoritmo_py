def main():
    numeros_reais = []
    qtd_negativos = 0
    soma_positivos = 0

    for _ in range(10):
        n = int(input())

        if n >= 0:
            soma_positivos += n
        else:
            qtd_negativos += 1

        numeros_reais.append(n)
    
    print(numeros_reais)
    print(qtd_negativos)
    print(soma_positivos)

if __name__ == "__main__":
    main()