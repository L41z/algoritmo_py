def main():
    alunos = []
    soma_alturas = 0
    
    for _ in range(30):
        nome = input().strip()
        idade = int(input())
        altura = float(input())

        # indices [0], [1], [2]
        alunos.append((nome, idade, altura))
        soma_alturas += altura
    
    media_alturas = soma_alturas / len(alunos)

    menores_que_a_media = []
    for aluno in alunos:
        if aluno[1] > 13 and aluno[2] < media_alturas:
            menores_que_a_media.append(aluno[0])

    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    for aluno in menores_que_a_media:
        print(aluno)

if __name__ == "__main__":
    main()