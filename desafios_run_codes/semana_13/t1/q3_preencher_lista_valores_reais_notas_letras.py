def tarefa_a(n):
    valores = []
    for _ in range(n):
        valores.append(float(input()))

    valores_invertidos = [round(valor, 4) for valor in reversed(valores)]
    print(valores_invertidos)

def tarefa_b(n):
    notas = []
    for _ in range(n):
        notas.append(float(input()))

    notas_arredondadas = [round(nota, 1) for nota in notas]
    print(notas_arredondadas)
    
    if n == 0:
        print("SEM NOTAS")
    else:
        media = sum(notas) / n
        print(round(media, 1))

def tarefa_c(n):
    letras = []
    for _ in range(n):
        letra = input().strip()
        if letra:
            letras.append(letra[0])

    quantidade_vogais = 0
    consoantes = []
    vogais = "aeiouAEIOU"

    for letra in letras:
        if letra.isalpha(): 
            if letra in vogais:
                quantidade_vogais += 1
            else:
                consoantes.append(letra)

    print(quantidade_vogais)
    print(consoantes)

def main():
    n = int(input())

    if n >= 0:
        tarefa_a(n)
        tarefa_b(n)
        tarefa_c(n)

if __name__ == "__main__":
    main()