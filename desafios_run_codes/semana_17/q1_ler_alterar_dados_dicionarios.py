def ler_dicionario():
    dicionario = {}
    
    while True:
        try:
            chave = input().strip()
            if chave == "":
                break
            valor = input().strip()
            dicionario[chave] = valor
        except EOFError:
            break
    
    return dicionario

def atualizar_dicionario(dicionario):
    while True:
        try:
            chave = input().strip()
            if chave == "":
                break
            valor = input().strip()
            dicionario[chave] = valor
        except EOFError:
            break

def main():
    dicionario = ler_dicionario()
    print(dicionario)
    
    atualizar_dicionario(dicionario)
    print(dicionario)

if __name__ == "__main__":
    main()