def main():
    tx_rendimento = 0.007
    # taxa sobre o valor do carro que sobe 0.4% ao mes
    tx_valor_do_carro = 0.004

    valor_investido = 10000
    # copia_valor_investido = valor_investido

    qtd_meses = 0

    valor_do_carro = float(input())
    # copia_valor_do_carro = valor_do_carro

    while valor_investido < valor_do_carro:
        valor_investido += valor_investido * tx_rendimento
        valor_do_carro += valor_do_carro * tx_valor_do_carro
        qtd_meses += 1
    
    # print("Valor do carro: R$ {:.2f}".format(copia_valor_do_carro))
    # print("Valor investido: R$ {:.2f}".format(copia_valor_investido))
    # print("Quantidade de meses: {}".format(qtd_meses))

    print(qtd_meses)

if __name__ == "__main__":
    main()