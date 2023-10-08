url = 'https://bytebank.com/cambio?moedaOrigem=real'
print(url)
indice_interrogacao = url.find('?')

# O primeiro parâmetro é omitido também.
url_base = url[:indice_interrogacao]
print(url_base)

# O primeiro parâmetro do fatiamento da url é acrescentado de 1 porque ele
# é inclusivo e ira imprimir o '?. O segundo parâmetro será omitido'
url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)
