
class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b

# Chamando o método estático diretamente na classe
resultado = Calculadora.somar(5,3)

print("Resultado da soma:", resultado)


class Conta:
    def __init__(self,codigo,saldo):
        self.codigo= codigo
        self.saldo=saldo

while True:
    lista_de_contas=[]
    try:
        codigo_da_conta=int(input('informe o código da conta:'))
        saldo_da_conta=float(input('Informe o saldo da conta:'))
        conta_criada=Conta(codigo_da_conta,saldo_da_conta)
        lista_de_contas.append(conta_criada)

        for item in lista_de_contas:
            print(f'Código da conta:{item.codigo}\nSaldo da conta:{item.saldo}')



    except:
        print('Erro')
        input('Digite uma tecla para voltar')







     