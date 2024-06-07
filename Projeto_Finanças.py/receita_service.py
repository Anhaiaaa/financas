#Cadastrar receita
#Listar receitas 
#Excluir receita
#Editar receita
import os
from dados import dados_receita
from Receita import Receita
import uuid

def Menu_Receita():
    os.system('cls')
    print('-'*22)
    print(' '*5,'RECEITA')
    print('-'*22)
    print('1-Cadastrar receita')
    print('2-Listar receitas')
    print('3-Excluir receita')
    print('4-Editar receita')
    try:
        opcao_receita=int(input('Selecione uma opção:'))
        if opcao_receita==1:
            Cadastrar_receita()
            pass

        if opcao_receita==2:
            Listar_receita_menu_principal()
            pass

        if opcao_receita==3:
            Excluir_receita()
            pass
        
        
    except ValueError():
        print('ERRO')
        print(input('Digite uma tecla para voltar ao menu principal'))

def Cadastrar_receita():
    os.system('cls')
    print('-'*28)
    print(' '*4,'CADASTRAR RECEITA')
    print('-'*28)
    try:
        nome_da_receita=str(input('Digite o nome da receita:'))
        valor_da_receita=float(input('Digite o valor da despesa:'))

        descricao_receita=str(input('Informe a descrição da despesa:'))

        vencimento_da_receita=str(input('Informe a data de vencimento da receita:'))


        receita1=Receita(uuid.uuid4(),nome_da_receita,valor_da_receita,descricao_receita,vencimento_da_receita)
        dados_receita.append(receita1)

        print('Receita cadastrada com sucesso!')
        input('Digite uma tecla para voltar ao menu principal:')

    except:
        print('ERRO, valor inválido')
        input('Digite uma tecla para voltar ao menu principal:')

def Listar_receitas():
    os.system('cls')
    print('-'*22)
    print(' '*5,'RECEITAS')
    print('-'*22)
    cont=0
    for receita_item in dados_receita:
        cont+=1
        print(f'{cont}-{receita_item.nome} R$ {receita_item.valor}\nDescrição:{receita_item.descricao}\n')

def Listar_receita_menu_principal():
    Listar_receitas()
    input('Digite uma tecla para voltar ao menu principal:')

def Excluir_receita():
    os.system('cls')
    print('-'*22)
    print('EXCLUIR RECEITA')
    print('-'*22)
    
    try:
        Listar_receitas()
        receita_excluida_pelo_usuario=int(input('Qual despesa deseja excluir?'))
        dados_receita.pop(receita_excluida_pelo_usuario-1)

        print('Receita excluida com sucesso!')
        input('Digite uma tecla para voltar ao menu principal:')

    except ValueError:
        print('Erro, valor inválido!')
        input('Digite uma tecla para voltar ao menu principal:')

def Editar_receita():
    pass
    

