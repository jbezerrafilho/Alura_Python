import re  # Regular Expression -- RegEx

endereco = "Rua Torres Galvão, 85 59032160"

'''
    Como represento um CEP?
    5 dígitos - hífen (opcional) - 3 dígitos
'''

# Dentro de colchetes o dígito pode assumir qualquer valor
pattern = re.compile(
    "[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")

# As chaves quantifica os digítos no padrão
pattern1 = re.compile("[0123456789]{5}[-]?[0123456789]{3}")

# Dentro dos cochetes podemos definir o intervalo
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)
