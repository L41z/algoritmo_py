def main():
    tx_natalidade_a = 0.02
    tx_natalidade_b = 0.03

    # populacao de A > populacao de B
    pop_a = int(input())
    pop_b = int(input())

    # se a população de A for menor que a população de B, inverta os valores
    if pop_a < pop_b:
        pop_a, pop_b = pop_b, pop_a

    anos = 0
    while pop_a > pop_b:
        pop_a += int(pop_a * tx_natalidade_a)
        pop_b += int(pop_b * tx_natalidade_b)
        anos += 1
    print(anos)

if __name__ == "__main__":
    main()