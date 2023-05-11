import random


def jogar():
    print("***************************************")
    print("** Bem vindo ao jogo de Adivinhação! **")
    print("***************************************")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Selecione a dificuldade do jogo, sendo:")
    print("(1) - Fácil - (2) Médio - (3) Difícil")

    while True:
        try:
            nivel = int(input("> "))
            if nivel == 1:
                total_de_tentativas = 20
                break
            elif nivel == 2:
                total_de_tentativas = 10
                break
            elif nivel == 3:
                total_de_tentativas = 5
                break
            else:
                print("Digite apenas as opções (1), (2) ou (3).")
        except ValueError:
            print("Digite apenas números inteiros (1), (2) ou (3).")

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")

        chute_str = input("Digite um número entre 1 e 100: ")
        print(f"Você digitou {chute_str}")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto.\n")
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto.\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
