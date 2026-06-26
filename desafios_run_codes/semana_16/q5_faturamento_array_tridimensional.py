def ler_dados():
    num_anos = 4
    num_filiais = 3
    num_meses = 12
    
    dados = []
    
    for ano in range(num_anos):
        ano_dados = []
        for filial in range(num_filiais):
            filial_dados = []
            for mes in range(num_meses):
                filial_dados.append(int(input()))
            ano_dados.append(filial_dados)
        dados.append(ano_dados)
    
    return dados

def calcular_totais(dados):
    num_anos = len(dados)
    num_filiais = len(dados[0])
    
    total_ano_filial = []
    for ano in range(num_anos):
        ano_totais = []
        for filial in range(num_filiais):
            total = sum(dados[ano][filial])
            ano_totais.append(total)
        total_ano_filial.append(ano_totais)
    
    total_todas_filiais_ano = []
    for ano in range(num_anos):
        total = sum(total_ano_filial[ano])
        total_todas_filiais_ano.append(total)
    
    total_periodo = sum(total_todas_filiais_ano)
    
    return total_ano_filial, total_todas_filiais_ano, total_periodo

def main():
    dados = ler_dados()
    
    anos = [2014, 2015, 2016, 2017]
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    num_anos = len(dados)
    num_filiais = len(dados[0])
    
    total_ano_filial, total_todas_filiais_ano, total_periodo = calcular_totais(dados)
    
    for ano in range(num_anos):
        for filial in range(num_filiais):
            for mes in range(12):
                print(f"{anos[ano]};Filial {filial + 1};{meses[mes]};{dados[ano][filial][mes]}")
            print(f"TOTAL {anos[ano]} FILIAL {filial + 1};{total_ano_filial[ano][filial]}")
        print(f"TOTAL {anos[ano]} TODAS FILIAIS;{total_todas_filiais_ano[ano]}")
    
    print(f"TOTAL PERÍODO TODAS FILIAIS;{total_periodo}")

if __name__ == "__main__":
    main()