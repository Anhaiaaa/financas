
lista_objetos=[]
lista_despesa=[]


class Usuario():
    def __init__(self,nome,saldo):
        self.nome=nome
        self.saldo=saldo


def cadastrar_usuario():
    nome_do_usuario=str(input('Digite o nome do usuario:')).lower()
    saldo_do_usuario=float(input('Digite o saldo da conta:'))
    usuario_criado=Usuario(nome_do_usuario,saldo_do_usuario)
    lista_objetos.append(usuario_criado)

    print('Usuario adicionado com sucesso')


def mostrar_saldo():
    for usuario,despesa in zip(lista_objetos,lista_despesa):
        print(f'SALDO: {usuario.saldo[-1]-despesa}')

def Despesa():
    despesa_criada=float(input('Digite o valor da despesa:'))
    lista_despesa.append(despesa_criada)


while True:
    
    opcao=int(input('Digite um opção'))  

    if opcao==1:
        cadastrar_usuario()

    if opcao==2:
        mostrar_saldo()

    if opcao==3:
        Despesa()
     