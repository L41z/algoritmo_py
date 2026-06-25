def soma_cumulativa(lista):
    resultado = []
    soma = 0
    for num in lista:
        soma += num
        resultado.append(soma)
    return resultado

def main():
    numeros = []
    
    while True:
        n = int(input())
        if n == 0:
            break
        numeros.append(n)
        
    lista_cumulativa = soma_cumulativa(numeros)
    print(lista_cumulativa)

if __name__ == "__main__":
    main()