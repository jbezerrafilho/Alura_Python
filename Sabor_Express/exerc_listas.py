# Criando listas

decimais = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Zezinho', 'Paty', 'Gaby', 'Belle']
anos = [1977, 2023]

print('Percorrendo a lista de decimais')

for i in decimais:
    print(i)

print('Calculando a soma de números ímpares entre 1 e 10')

soma_impares = 0
for j in range(1, 11, 2):
    soma_impares = soma_impares + j
print(soma_impares)

print('Imprimindo uma lista de 1 a 10 em ordem decrescente')

for k in range(10, 0, -1):
    print(k)

print('Imprimindo a tabuada de um número')

numero = int(input('Digite um número para ver sua tabuada:\n'))
for m in range(1, 11):
    resultado = numero * m
    print(f'{numero} * {m} = {resultado}')

print('Criando uma lista para trabalhar com Excessões: ')
lista_numeros = [5, 10, 8, 9, 7, 3]
soma = 0
try:
    for n in lista_numeros:
        soma += n
    print(f'Soma dos números da lista: {soma}')
except Exception as e:
    print(f'Ocorreu o erro {e}')
