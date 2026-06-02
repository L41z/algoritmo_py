def main():
    # formato ddmmaaaa
    dt_nasc = int(input())

    numero_da_sorte = 0

    while dt_nasc != 0:
        numero_da_sorte += dt_nasc % 10
        dt_nasc //= 10
    print(numero_da_sorte)

if __name__ == "__main__":
    main()