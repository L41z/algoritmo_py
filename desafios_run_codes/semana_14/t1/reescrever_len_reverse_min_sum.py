def comprimento(lista):
    tam = 0

    for _ in lista:
        tam += 1

    return tam

def inverter(lista):
    lista_invertida = []

    for item in lista:
        lista_invertida.insert(0, item)

    return lista_invertida

def minimo(lista):
    menor = lista[0]

    for item in lista:
        if item < menor:
            menor = item
    
    return menor

def maximo(lista):
    maior = lista[0]

    for item in lista:
        if item > maior:
            maior = item
    
    return maior

def soma(lista):
    soma = 0

    for item in lista:
        soma += item
    
    return soma

def main():
    lista = []
    while True:
        n = int(input())

        if n > 0:
            lista.append(n)
        else:
            break

    print(lista)
    print(comprimento(lista))
    print(inverter(lista))
    print(minimo(lista))
    print(maximo(lista))
    print(soma(lista))

if __name__ == "__main__":
    main()