def ler_dados():
    fabricantes = ["Fiat", "Ford", "GM", "Wolkswagen"]
    anos = [2013, 2014, 2015, 2016, 2017, 2018]
    vendas = []
    
    numeros = []
    while True:
        try:
            linha = input().strip()
            if linha == '':
                break
            numeros.append(int(linha))
        except EOFError:
            break
        except ValueError:
            break
    
    ano = numeros[-1]
    numeros = numeros[:-1]
    
    for i in range(4):
        linha = []
        for j in range(6):
            linha.append(numeros[i * 6 + j])
        vendas.append(linha)
    
    return fabricantes, anos, vendas, ano

def fabricante_mais_vendeu_ano(vendas, fabricantes, ano, anos):
    idx_ano = anos.index(ano)
    max_vendas = -1
    fabricante = ""
    
    for i in range(len(fabricantes)):
        if vendas[i][idx_ano] > max_vendas:
            max_vendas = vendas[i][idx_ano]
            fabricante = fabricantes[i]
    
    return fabricante, max_vendas

def ano_maior_volume(vendas, anos):
    totais = []
    
    for j in range(len(anos)):
        total = 0
        for i in range(len(vendas)):
            total += vendas[i][j]
        totais.append(total)
    
    idx_maior = totais.index(max(totais))
    return anos[idx_maior], totais[idx_maior]

def medias_anuais_fabricantes(vendas, fabricantes, anos):
    medias = []
    
    for i in range(len(fabricantes)):
        soma = sum(vendas[i])
        media = soma / len(anos)
        medias.append(round(media, 2))
    
    return medias

def main():
    fabricantes, anos, vendas, ano = ler_dados()
    
    fabricante, vendas_ano = fabricante_mais_vendeu_ano(vendas, fabricantes, ano, anos)
    print(f"A fabricante que mais vendeu em {ano} foi a {fabricante} com {vendas_ano} mil unidades.")
    
    ano_volume, total_volume = ano_maior_volume(vendas, anos)
    print(f"O ano de maior volume geral de vendas foi {ano_volume} com {total_volume} mil unidades.")
    
    medias = medias_anuais_fabricantes(vendas, fabricantes, anos)
    print("A média anual de vendas de cada fabricante entre 2013 e 2018 foi:")
    for i in range(len(fabricantes)):
        if medias[i] == int(medias[i]):
            print(f"A {fabricantes[i]} vendeu em média {int(medias[i])}.0 unidades por ano.")
        else:
            print(f"A {fabricantes[i]} vendeu em média {medias[i]} unidades por ano.")

if __name__ == "__main__":
    main()