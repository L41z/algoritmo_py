def main():
    soma = 0
    multiplicacao = 1
    lista = []
    
    for i in range(10):
        n = int(input())
        lista.append(n)
        soma += n
        multiplicacao *= n

    print(lista)
    print(soma)
    print(multiplicacao)
    
if __name__ == "__main__":
    main()