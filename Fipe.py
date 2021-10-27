import requests

class Fipe:
    def __init__(self, codigo):
        self.__informacoes = self.__busca_informacoes(codigo)
        self.__valor = self.__informacoes['valor']
        self.__marca = self.__informacoes['marca']
        self.__modelo = self.__informacoes['modelo']
    

    @staticmethod
    def __busca_informacoes(codigo):
        codigo = str(codigo).strip()
        url = f'https://brasilapi.com.br/api/fipe/preco/v1/{codigo}'
        r = requests.get(url)

        if r.status_code == 400:
            raise ValueError(f'O Código "{codigo}" é inválido ou inexistente')
        else:
            return r.json()[0]
    

    @property
    def valor(self):
        return self.__valor
    

    @property
    def marca(self):
        return self.__marca
    

    @property
    def modelo(self):
        return self.__modelo
    
