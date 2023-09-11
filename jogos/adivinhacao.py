import random

print('********************')
print("Jogo de adivinhação")
print('********************')
numero_secreto = random.randint(1, 100)

total_tentativas = 0
print("Defina o nível do jogo: ", numero_secreto)
print("1 - Fácil, 2 - Médio, 3 - Difícil")
level = int(input("Qual a sua escolha: "))
pontos = 1000

if level == 1:
    total_tentativas = 20
elif level == 2:
    total_tentativas = 10
else:
    total_tentativas = 5

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
        print('Você acertou e sua pontuação foi {}!'.format(pontos))
        break
    else:
        if maior:
            print('Você errou! Seu chute foi maior que o número secreto!')
        elif menor:
            print('Você errou! Seu chute foi menor que o número secreto!')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim de Jogo!")