def ler_matriz(n, m):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(int(input()))
        matriz.append(linha)
    return matriz

def calcular_soma_primeira_linha(matriz):
    return sum(matriz[0])

def calcular_soma_ultima_coluna(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][-1]
    return soma

def calcular_media(matriz):
    soma = 0
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
            total += 1
    return round(soma / total, 4)

def encontrar_menor(matriz):
    menor = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
    return menor

def encontrar_maior(matriz):
    maior = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    return maior

def main():
    n = int(input())
    m = int(input())
    
    matriz = ler_matriz(n, m)
    
    soma_primeira_linha = calcular_soma_primeira_linha(matriz)
    soma_ultima_coluna = calcular_soma_ultima_coluna(matriz)
    media = calcular_media(matriz)
    menor = encontrar_menor(matriz)
    maior = encontrar_maior(matriz)
    
    resultado = (soma_primeira_linha, soma_ultima_coluna, media, menor, maior)
    print(resultado)

if __name__ == "__main__":
    main()