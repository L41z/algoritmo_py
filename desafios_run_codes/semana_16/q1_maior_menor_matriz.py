def ler_matriz(n):
    matriz = []

    for i in range(n):
        linha = []
        for j in range(n):
            valor = int(input())
            linha.append(valor)
        matriz.append(linha)
    return matriz

def encontrar_posicoes_maior_menor(matriz):
    tam = len(matriz)

    maior = matriz[0][0]
    menor = matriz[0][0]
    pos_maior = (0, 0)
    pos_menor = (0, 0)

    for i in range(tam):
        for j in range(tam):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                pos_maior = (i, j)
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                pos_menor = (i, j)
    
    return (pos_maior, pos_menor)

def exibir_matriz(matriz):
    for linha in matriz:
        print("  ".join(f"{elem:4d}" for elem in linha))

def main():
    ordem = int(input())

    matriz = ler_matriz(ordem)

    posicoes = encontrar_posicoes_maior_menor(matriz)

    for posicao in posicoes:
        print(posicao)
    
if __name__ == "__main__":
    main()