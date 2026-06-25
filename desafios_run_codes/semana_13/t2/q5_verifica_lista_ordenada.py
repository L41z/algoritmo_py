def esta_ordenado(lista):
    return lista == sorted(lista)

def main():
    tam = int(input())

    lista = []
    for _ in range(tam):
        
        n = float(input())
        lista.append(n)

    if esta_ordenado(lista):
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")

if __name__ == "__main__":
    main()