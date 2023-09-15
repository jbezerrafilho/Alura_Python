def jogar():
    print("***************************")
    print("***** Jogo da Forca *******")
    print("***************************")

    palavra_secreta = "banana".upper()
    letras_certas = ["_" for letra in palavra_secreta]
    # letras_certas = []
    # # for letra in palavra_secreta:
    # #     letras_certas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    print(letras_certas)
    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_certas[index] = letra
                    print("Encontrei a letra '{}' na posição {}".format(letra, index))
                index = index + 1
        else:
            erros = erros + 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_certas
        print(letras_certas)

        print("jogando...")

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")


if __name__ == "__main__":
    jogar()
