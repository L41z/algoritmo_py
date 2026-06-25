def main():
    x = []

    for _ in range(5):
        n = int(input())

        x.append(n)

    y = []
    for _ in range(5):
        n = int(input())

        y.append(n)

    equacao = ""
    produto_escalar = 0
    for i in range(5):
        equacao += f"({x[i]} x {y[i]}) + "
        produto_escalar += x[i] * y[i]

        if i == 4:
            equacao += f"({x[i]} x {y[i]}) = {produto_escalar}"

    
    print(x)
    print(y)
    print(equacao)

if __name__ == "__main__":
    main()