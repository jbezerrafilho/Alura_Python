# url = 'https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'
url = ""

# Sanitizando uma url (Removendo espaços em brancos e caracteres especiais)
url = url.strip()

# Validando a url
if url == "":
    raise ValueError("A URL está vazia")

# Separa base dos parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]

# Busca o valor do parâmetro
busca_parametro = 'moedaOrigem'
indice_parametros = url_parametros.find(busca_parametro)
indice_valor_parametro = indice_parametros + len(busca_parametro) + 1
indice_e_comercial = url_parametros.find('&', indice_valor_parametro)

if indice_e_comercial == -1:
    valor_parametro = url_parametros[indice_valor_parametro:]
else:
    valor_parametro = url_parametros[indice_valor_parametro: indice_e_comercial]

print(valor_parametro)

