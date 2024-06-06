#Cadastrar despesa
#Listar despesas 
#Excluir despesa
#Editar despesa
from dados import despesas
from Despesa import Despesa
import uuid
import os

def Menu_Despesas():
    os.system('cls')
    print('-'*22)
    print(' '*5,'DESPESAS')
    print('-'*22)
    print('1-Cadastrar despesa')
    print('2-Listar despesas')
    print('3-Excluir despesa')
    print('4-Editar despesa')
    try:
        opcao_despesas=int(input('Selecione uma opção:'))
        if opcao_despesas==1:
            Cadastrar_despesa()

        if opcao_despesas==2:
             Listar_despesas_voltar_menu_principal()
        if opcao_despesas==3:
             Excluir_despesas()
             
    except ValueError():
            print('Valor inválido, erro na digitação!')
            input('Digite uma tecla para voltar ao menu principal')
        
    pass


def Cadastrar_despesa():
    os.system('cls')
    print('-'*28)
    print(' '*4,'CADASTRAR DESPESAS')
    print('-'*28)
    try:
        nome_da_despesa= str(input('Digite o nome da despesa:')).capitalize()
        valor_da_despesa=float(input('Digite o valor da despesa:'))

        despesa1=Despesa(uuid.uuid4(),nome_da_despesa,valor_da_despesa)
        despesas.append(despesa1)

        print('Despesa cadastrada com sucesso!')
        input('Digite uma tecla para voltar ao menu principal:')
    except ValueError:
         pass

def Listar_despesas():
    os.system('cls')
    print('-'*22)
    print(' '*6,'GASTOS')
    print('-'*22)
    cont=0
    for despesa_item in despesas:
            cont+=1
            
            print(f'{cont}-{despesa_item.nome} R$ {despesa_item.valor}')
            

def Listar_despesas_voltar_menu_principal():
     Listar_despesas()
     input('Digite uma tecla para voltar ao menu principal')
     




def Excluir_despesas():
    os.system('cls')
    try:
        Listar_despesas()
        despesa_excluida_pelo_usuario=int(input('Qual despesa deseja excluir?'))
        despesas.pop(despesa_excluida_pelo_usuario-1)

        print('Despesa excluída com sucesso!')
        input('Digite uma tecla para voltar ao menu principal:')
       
    except ValueError:
        print('Erro, valor inválido!')
        input('Digite uma tecla para voltar ao menu principal:')
        pass



def Editar_despesa():
    pass

   