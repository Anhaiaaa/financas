#Cadastrar conta
#Listar contas
#Excluir conta
#Editar conta
import os
from Conta import Conta
from dados import lista_contas, lista_despesas, dados_receita
import uuid

def Menu_Conta():
    os.system('cls')
    print('-'*22)
    print(' '*7,'CONTA')
    print('-'*22)
    print('1-Cadastrar Conta')
    print('2-Listar Contas')
    print('3-Excluir Conta')
    print('4-Editar Conta')
    opcao_contas=int(input('Selecione uma opção:'))
    if opcao_contas==1:
        Cadastrar_conta()

    if opcao_contas==2:
        Listar_contas_menu_principal()

def mostrar_saldo():

    for conta in lista_contas:
        saldo=conta.saldo

    for despesa_item in lista_despesas:
            saldo = saldo - despesa_item.valor
    
    for receita_item in dados_receita:
        saldo = saldo + receita_item.valor
    print(f'SALDO ATUAL: R${saldo:.2f}')

    
def Cadastrar_conta():
     os.system('cls')
     print('-'*28)
     print(' '*4,'CADASTRAR CONTA')
     print('-'*28)
     try:

        nome_conta=str(input('Informe o Nome da Conta:')).lower()
        saldo_conta=0
        
        conta_criada=Conta(uuid.uuid4(),saldo_conta,nome_conta)
        lista_contas.append(conta_criada)

        print('\nConta cadastrada com sucesso!')
        input('Digite uma tecla para voltar ao menu principal:')

     except ValueError:
        print('ERRO, valor inválido!')
        input('Digite uma tecla para voltar ao menu principal:')


    
def Listar_contas():
    print('-'*28)
    print('CONTAS')
    print('-'*28)
    for  conta in lista_contas:
            print(f'ID-{conta.id}\nNOME:{conta.nome}')
    mostrar_saldo()
            
    

def Listar_contas_menu_principal():
    os.system('cls')
    Listar_contas()
    input('Digite uma tecla para voltar ao menu principal')
            

def Excluir_conta():
    pass

def Editar_conta():
    pass

