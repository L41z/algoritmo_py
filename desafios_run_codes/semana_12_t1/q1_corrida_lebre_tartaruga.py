def main():
    velocidade_tartaruga = 1
    velocidade_lebre = 10

    # distancia que a tartaruga sai a frente da lebre
    distancia = int(input())

    tempo = 0
    while distancia > 0:
        # a cada 1 minuto, a tartaruga anda 1 metro e a lebre anda 10 metros
        distancia -= (velocidade_lebre - velocidade_tartaruga)
        tempo += 1
    # print("A lebre alcançou a tartaruga!")
    # print(f"Tempo gasto: {tempo} minutos")
    print(tempo)

if __name__ == "__main__":
    main()