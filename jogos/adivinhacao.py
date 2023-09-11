print('********************')
print("Jogo de adivinhação")
print('********************')
numero_secreto = 45

total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute = input("digite o seu número: ")
    print("Você digitou: ", chute)
    chute = int(chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 0 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if numero_secreto == chute:
        print('Você acertou!')
        break
    else:
        if maior:
            print('Você errou! Seu chute foi maior que o número secreto!')
        elif menor:
            print('Você errou! Seu chute foi menor que o número secreto!')


print("Fim de Jogo!")