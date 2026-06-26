def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado


cidades = carrega_cidades()

def main():
    valor = int(input())

    print(f"CIDADES COM MAIS DE {valor} HABITANTES:")
    for cidade in cidades:
        if cidade[5] > valor:
            print(f"IBGE: {cidade[1]} - {cidade[2]}({cidade[0]}) - POPULAÇÃO: {cidade[5]}")

if __name__ == "__main__":
    main()