import random


def jogar():
    mensagem_abertura()
    palavras = criando_lista_palavras()
    palavra = palavra_secreta(palavras)
    lacunas = lacunas_palavra(palavra)

    enforcou = False
    acertou = False
    erros = 0

    print(lacunas)
    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra:
            marca_chute_correto(chute, palavra, lacunas)
        else:
            erros = erros + 1
            desenha_forca(erros)
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in lacunas
        print(lacunas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra)


def mensagem_abertura():
    print("***************************")
    print("***** Jogo da Forca *******")
    print("***************************")


def criando_lista_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    return palavras


def palavra_secreta(palavras):
    numero = random.randrange(0, len(palavras))
    palavra = palavras[numero].upper()
    return palavra


def lacunas_palavra(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra, lacunas):
    index = 0
    for letra in palavra:
        if chute == letra:
            lacunas[index] = letra
            print("Encontrei a letra '{}' na posição {}".format(letra, index))
        index = index + 1


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
