def main():
    notas = []
    for _ in range(50):
        notas.append(float(input()))

    indices_aprovados = []
    for i in range(len(notas)):
        if notas[i] >= 6:
            indices_aprovados.append(i)

    print(indices_aprovados)

if __name__ == "__main__":
    main()