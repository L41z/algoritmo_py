def cadastrar_pessoas():
    pessoas = {}
    
    for i in range(20):
        nome = input().strip()
        idade = int(input())
        cpf = input().strip()
        
        pessoas[cpf] = {
            'nome': nome,
            'idade': idade,
            'cpf': cpf
        }
    
    return pessoas

def separar_menores(pessoas):
    maiores = {}
    menores = {}
    
    for cpf, dados in pessoas.items():
        if dados['idade'] >= 18:
            maiores[cpf] = dados
        else:
            menores[cpf] = dados
    
    return maiores, menores

def imprimir_dicionario(dicionario, titulo):
    print(f"========== {titulo} ==========")
    for cpf, dados in dicionario.items():
        print(f"{dados['nome']};{dados['idade']};{dados['cpf']}")

def main():
    pessoas = cadastrar_pessoas()
    maiores, menores = separar_menores(pessoas)
    
    imprimir_dicionario(maiores, "MAIORES DE 18 ANOS")
    imprimir_dicionario(menores, "MENORES DE 18 ANOS")

if __name__ == "__main__":
    main()