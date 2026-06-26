def obter_maior_temperatura(temperaturas):
    maior_temperatura = temperaturas[0]

    for temperatura in temperaturas:
        if temperatura[1] == 'C':
            if maior_temperatura[1] == 'C':
                if temperatura[0] > maior_temperatura[0]:
                    maior_temperatura = temperatura
            else:
                if temperatura[0] > (maior_temperatura[0] - 32) * 5 / 9:
                    maior_temperatura = temperatura
        else:
            if maior_temperatura[1] == 'C':
                if (temperatura[0] - 32) * 5 / 9 > maior_temperatura[0]:
                    maior_temperatura = temperatura
            else:
                if temperatura[0] > maior_temperatura[0]:
                    maior_temperatura = temperatura

    return maior_temperatura

def main():
    temperaturas = []

    for _ in range(2):
       valor = float(input())
       escala = input().strip().upper()[0]
       temperaturas.append((valor, escala))

    maior_temperatura = obter_maior_temperatura(temperaturas)
    print(f"({maior_temperatura[0]}, '{maior_temperatura[1]}')")

if __name__ == "__main__":
    main()