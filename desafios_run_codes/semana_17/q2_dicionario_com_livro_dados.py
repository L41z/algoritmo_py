def ler_livros():
    livros = {}
    codigo = 101
    
    while True:
        try:
            titulo = input().strip()
            if titulo == "":
                break
            
            isbn = input().strip()
            autor = input().strip()
            preco = float(input().strip())
            
            livros[codigo] = {
                'titulo': titulo,
                'isbn': isbn,
                'autor': autor,
                'preco': preco
            }
            codigo += 1
        except EOFError:
            break
    
    return livros

def imprimir_livros(livros):
    for codigo, dados in livros.items():
        print(f"Código: {codigo}")
        print(f"Título: {dados['titulo']}")
        print(f"ISBN: {dados['isbn']}")
        print(f"Autor: {dados['autor']}")
        print(f"Preço: {dados['preco']:.2f}")

def main():
    livros = ler_livros()
    imprimir_livros(livros)

if __name__ == "__main__":
    main()