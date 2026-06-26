def obter_temperaturas():
    temperaturas = []
    dados = []
    
    while True:
        try:
            linha = input().strip()
            if linha == '':
                break
            dados.append(linha)
        except EOFError:
            break
    
    for i in range(0, len(dados), 2):
        if i + 1 < len(dados):
            valor = float(dados[i])
            unidade = dados[i + 1].upper()
            mes = (i // 2) + 1
            temperaturas.append((mes, valor, unidade))
    
    return temperaturas

def converter_para_kelvin(valor, unidade):
    if unidade == 'C':
        return valor + 273.15
    elif unidade == 'F':
        return (valor - 32) * 5/9 + 273.15
    elif unidade == 'K':
        return valor
    else:
        return valor

def meses_por_extenso():
    return {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

def calcular_media_anual(temperaturas):
    soma = 0
    for mes, valor, unidade in temperaturas:
        soma += converter_para_kelvin(valor, unidade)
    return soma / 12

def formatar_temperatura(valor):
    return f"{valor:.2f}".rstrip('0').rstrip('.')

def main():
    temperaturas = obter_temperaturas()
    
    media_anual = calcular_media_anual(temperaturas)
    print(f"TEMPERATURA MÉDIA ANUAL")
    print(f"{formatar_temperatura(media_anual)}K")
    
    meses = meses_por_extenso()
    print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
    
    for mes, valor, unidade in temperaturas:
        temp_kelvin = converter_para_kelvin(valor, unidade)
        if temp_kelvin > media_anual:
            print(f"{meses[mes]}: {formatar_temperatura(temp_kelvin)}K")

if __name__ == "__main__":
    main()