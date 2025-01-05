
class Marmita():
    def __init__(self,tamanho,preco):
        self.tamanho=tamanho
        self.preco=float(preco)

    def mostrar_informaçoes(self):
        return f'Tamanho:{self.tamanho}\nPreço: {self.preco}'
    
    def verificar_tipo(self):
        if isinstance (self.preco,str):
            return'Tipo: Marmita'
        else:
            return'Tipo: Bebida'

class Bebida(Marmita):
    def __init__(self, tamanho, preco,ml):
        self.ml=int(ml)

        super().__init__(tamanho, preco)

    def verificar_tipo(self):
        return super().verificar_tipo() 

    
    def mostrar_informaçoes(self):
        return f'{super().mostrar_informaçoes()}\nML:{self.ml}'
    
    
    
prato=Marmita('P',(15.00))
print(prato.mostrar_informaçoes(),'\n',prato.verificar_tipo(),'\n')


bebida= Bebida('G',(8.00),(1000))
print(bebida.mostrar_informaçoes(),'\n',bebida.verificar_tipo(),'\n')

bebida2= Bebida('G',(9),(500))
print(bebida2.mostrar_informaçoes(),'\n',bebida2.verificar_tipo())

type(prato())
    
        