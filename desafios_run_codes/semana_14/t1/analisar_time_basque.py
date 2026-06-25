def main():
    jogadores = []

    for i in range(12):
        nome = input()
        altura = float(input())

        jogadores.append((nome, altura))
    
    nome_mais_alto = ""
    maior_altura = 0
    media_altura = 0
    soma_altura = 0
    for jogador in jogadores:
        soma_altura += jogador[1]
        if jogador[1] > maior_altura:
            maior_altura = jogador[1]
            nome_mais_alto = jogador[0]
    
    media_altura = soma_altura / len(jogadores)

    maiores_que_a_media = []
    for jogador in jogadores:
        if jogador[1] > media_altura:
            maiores_que_a_media.append((jogador[0], jogador[1]))

    print('JOGADOR MAIS ALTO DO TIME')
    print(nome_mais_alto)
    print(f"{maior_altura:.2f}")
    print('ALTURA MÉDIA DO TIME')
    print(f"{media_altura:.2f}")
    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    
    for jogador in maiores_que_a_media:
        print(jogador[0])
        print(f"{jogador[1]:.2f}")

if __name__ == "__main__":
    main()