def somar_temperaturas(temperaturas):
    valor1, escala1 = temperaturas[0]
    valor2, escala2 = temperaturas[1]

    if escala1 == escala2:
        soma = valor1 + valor2
        escala_final = escala2
        
    elif escala1 == 'C' and escala2 == 'F':
        valor1_convertido = (valor1 * 9 / 5) + 32
        soma = valor1_convertido + valor2
        escala_final = 'F'
        
    elif escala1 == 'F' and escala2 == 'C':
        valor1_convertido = (valor1 - 32) * 5 / 9
        soma = valor1_convertido + valor2
        escala_final = 'C'

    return (round(soma, 4), escala_final)

def main():
    temperaturas = []

    for _ in range(2):
        valor = float(input())
        escala = input().strip().upper()[0]
        temperaturas.append((valor, escala))

    resultado = somar_temperaturas(temperaturas)
    print(f"({resultado[0]}, '{resultado[1]}')")

if __name__ == "__main__":
    main()