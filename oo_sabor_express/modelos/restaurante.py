class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


r1 = Restaurante()
r1.nome = 'Bom ki só'
r1.categoria = 'caseiro'

r2 = Restaurante()

# print(r1, r2)
print(vars(r1))