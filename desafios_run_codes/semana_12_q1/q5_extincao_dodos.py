def main():
    populacao_inicial = int(input())
    ano = 1600

    limite_populacao = populacao_inicial * 0.10
    tt_populacao = populacao_inicial

    while tt_populacao > limite_populacao:
        # Usando arredondamento padrão (round) ou int() para ambos
        qtd_nascimentos = int(tt_populacao * 0.01)  # 1% da população
        qtd_mortes = int(tt_populacao * 0.06)       # 6% da população

        tt_populacao = tt_populacao + qtd_nascimentos - qtd_mortes
        
        # Garantindo que o ano e os valores sejam impressos como inteiros
        print(f"{ano},{qtd_nascimentos},{qtd_mortes},{int(tt_populacao)}")
        ano += 1

if __name__ == "__main__":
    main()