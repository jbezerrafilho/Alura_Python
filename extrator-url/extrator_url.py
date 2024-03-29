import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")
        pattern = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = pattern.match(url)

        if not match:
            raise ValueError("URL inválida!!!")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametros = self.get_url_parametros().find(parametro_busca)
        indice_valor_parametro = indice_parametros + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor_parametro)
        if indice_e_comercial == -1:
            valor_parametro = self.get_url_parametros()[indice_valor_parametro:]
        else:
            valor_parametro = self.get_url_parametros()[indice_valor_parametro: indice_e_comercial]
        return valor_parametro


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
# url = None
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("moedaDestino")
print(valor_quantidade)
