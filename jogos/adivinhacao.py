print('********************')
print("Jogo de adivinhação")
print('********************')
numero_secreto = 45

total_tentativas = 3
rodada = 1
while rodada <= total_tentativas:
    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute = input("digite o seu número: ")
    print("Você digitou: ", chute)
    chute = int(chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if numero_secreto == chute:
        print('Você acertou!')
    else:
        if maior:
            print('Você errou! Seu chute foi maior que o número secreto!')
        elif menor:
            print('Você errou! Seu chute foi menor que o número secreto!')

    rodada = rodada + 1

print("Fim de Jogo!")