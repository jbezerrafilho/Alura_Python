def jogar():
    print("***************************")
    print("***** Jogo da Forca *******")
    print("***************************")

    palavra_secreta = "banana"
    letras_certas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    print(letras_certas)
    while not enforcou and not acertou:
        chute = input("Qual a letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_certas[index] = letra
                print("Encontrei a letra '{}' na posição {}".format(letra, index))
            index = index + 1
        print(letras_certas)

        print("jogando...")


if __name__ == "__main__":
    jogar()
