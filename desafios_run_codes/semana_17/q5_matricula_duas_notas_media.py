def ler_alunos():
    alunos = {}
    
    while True:
        matricula = input().strip()
        if matricula == "":
            break
        
        nome = input().strip()
        nota1 = float(input())
        nota2 = float(input())
        
        alunos[matricula] = {
            'nome': nome,
            'nota1': nota1,
            'nota2': nota2
        }
    
    return alunos

def calcular_media(alunos, matricula):
    if matricula in alunos:
        media = (alunos[matricula]['nota1'] + alunos[matricula]['nota2']) / 2
        return media
    return None

def main():
    alunos = ler_alunos()
    
    while True:
        matricula = input().strip()
        if matricula == "":
            break
        
        media = calcular_media(alunos, matricula)
        if media is not None:
            print(f"{alunos[matricula]['nome']}: {media:.1f}")
        else:
            print("Aluno não encontrado")

if __name__ == "__main__":
    main()