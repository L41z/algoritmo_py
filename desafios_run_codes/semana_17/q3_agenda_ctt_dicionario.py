def ler_agenda(tamanho):
    agenda = {}
    
    for i in range(tamanho):
        nome = input().strip()
        cidade = input().strip()
        estado = input().strip()
        telefone = input().strip()
        
        agenda[nome] = {
            'cidade': cidade,
            'estado': estado,
            'telefone': telefone
        }
    
    return agenda

def imprimir_agenda(agenda):
    max_nome = max(len(nome) for nome in agenda.keys())
    max_cidade = max(len(f"{dados['cidade']}({dados['estado']})") for dados in agenda.values())
    max_telefone = max(len(dados['telefone']) for dados in agenda.values())
    
    for nome, dados in agenda.items():
        cidade_estado = f"{dados['cidade']}({dados['estado']})"
        print(f"{nome:<{max_nome + 12}} {cidade_estado:<{max_cidade + 10}} {dados['telefone']:>{max_telefone}}")

def main():
    tamanho = int(input())
    agenda = ler_agenda(tamanho)
    imprimir_agenda(agenda)

if __name__ == "__main__":
    main()