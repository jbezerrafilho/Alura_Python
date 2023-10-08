"""
    Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URL inválidas:
    https://bytebank/cambio
    http://bytebank.naoexiste/cambio
    ht:bytebank.naoexiste/cambio
"""

import re

url = "ttp://www.bytebank.com.br/cambio"
pattern = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = pattern.match(url)

if match:
    print("URL válida!")
else:
    print("URL inválida!!")
