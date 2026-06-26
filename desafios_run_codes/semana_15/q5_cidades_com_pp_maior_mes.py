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
    mes = int(input())
    valor = int(input())

    nome_mes = ""

    if mes == 1:
        nome_mes = "JANEIRO"
    elif mes == 2:
        nome_mes = "FEVEREIRO"
    elif mes == 3:
        nome_mes = "MARÇO"
    elif mes == 4:
        nome_mes = "ABRIL"
    elif mes == 5:
        nome_mes = "MAIO"
    elif mes == 6:
        nome_mes = "JUNHO"
    elif mes == 7:
        nome_mes = "JULHO"
    elif mes == 8:
        nome_mes = "AGOSTO"
    elif mes == 9:
        nome_mes = "SETEMBRO"
    elif mes == 10:
        nome_mes = "OUTUBRO"
    elif mes == 11:
        nome_mes = "NOVEMBRO"
    elif mes == 12:
        nome_mes = "DEZEMBRO"

    print(f"CIDADES COM MAIS DE {valor} HABITANTES E ANIVERSÁRIO EM {nome_mes}:")
    for cidade in cidades:
        if cidade[4] == mes and cidade[5] > valor:
            print(f"{cidade[2]}({cidade[0]}) tem {cidade[5]} habitantes e faz aniversário em {cidade[3]} de {nome_mes.lower()}.")
    
if __name__ == "__main__":
    main()