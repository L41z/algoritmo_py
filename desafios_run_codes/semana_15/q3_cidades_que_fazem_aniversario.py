# opcao mais elegivel com dicionario
def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append({
                'uf': uf,
                'ibge': int(ibge),
                'nome': nome,
                'dia': int(dia),
                'mes': int(mes),
                'pop': int(pop)
            })
    return resultado

def main():
    cidades = carrega_cidades()
    dia = int(input())
    mes = int(input())

    meses = {
        1: "JANEIRO", 2: "FEVEREIRO", 3: "MARÇO", 4: "ABRIL",
        5: "MAIO", 6: "JUNHO", 7: "JULHO", 8: "AGOSTO",
        9: "SETEMBRO", 10: "OUTUBRO", 11: "NOVEMBRO", 12: "DEZEMBRO"
    }

    nome_mes = meses.get(mes)

    print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {nome_mes}:")
    for cidade in cidades:
        if cidade['dia'] == dia and cidade['mes'] == mes:
            print(f"{cidade['nome']}({cidade['uf']})")

if __name__ == "__main__":
    main()