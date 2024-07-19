#Cadastrar receita
#Listar receitas 
#Excluir receita
#Editar receita
import os
from dados import dados_receita
from Receita import Receita
import uuid
import datetime
from menus import menu_editar_receita

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

        if opcao_receita==2:
            Listar_receita_menu_principal()
            
        if opcao_receita==3:
            Excluir_receita()
            
        if opcao_receita==4:
            Editar_receita()

        if opcao_receita>4:
            print('ERRO, valor inválido!')
            print(input('Digite uma tecla para voltar ao menu principal'))

        
        
    except ValueError():
        print('ERRO')
        print(input('Digite uma tecla para voltar ao menu principal'))

def Cadastrar_receita():
    os.system('cls')
    print('-'*28)
    print(' '*4,'CADASTRAR RECEITA')
    print('-'*28)
    try:
        nome_da_receita=str(input('Digite o nome da receita:')).capitalize()
        valor_da_receita=float(input('Digite o valor da receita:'))

        descricao_receita=str(input('\nInforme a descrição da receita:')).capitalize()

        vencimento_da_receita=input('\nInforme a data de vencimento da receita sem as barras ex:(01012024):')
        vencimento_da_receita_formatada= f'{vencimento_da_receita[0:2]}/{vencimento_da_receita[2:4]}/{vencimento_da_receita[4:]}'
        vencimento=datetime.datetime.strptime(vencimento_da_receita_formatada,"%d/%m/%Y")


        receita1=Receita(uuid.uuid4(),nome_da_receita,valor_da_receita,descricao_receita,vencimento)
        dados_receita.append(receita1)

        print('\nReceita cadastrada com sucesso!')
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
    for  indicie,receita_item in enumerate(dados_receita):
        
        print(f'{indicie+1}-{receita_item.nome} R$ {receita_item.valor:.2f}\nDescrição:{receita_item.descricao}\nVencimento:{receita_item.vencimento}\n')

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

        print('\nReceita excluida com sucesso!')
        input('Digite uma tecla para voltar ao menu principal:')

    except ValueError:
        print('Erro, valor inválido!')
        input('Digite uma tecla para voltar ao menu principal:')

def Editar_receita():
     
        try:
            Listar_receitas()
            receita_que_vai_ser_editada=int(input('Qual receita deseja editar?'))-1
            os.system('cls')
            menu_editar_receita()

            novo_nome_receita=str(input('Digite o novo nome da receita:')).capitalize()
            novo_valor_receita=float(input('Digite o novo valor da receita:'))
            nova_descrição_receita=str(input('\nDigite a descrição da receita:')).capitalize()
            nova_data_vencimento_receita=input('\nInforme a data de vencimento da receita sem as barras ex:(01012024):')
            vencimento_da_receita_formatada= f'{nova_data_vencimento_receita[0:2]}/{nova_data_vencimento_receita[2:4]}/{nova_data_vencimento_receita[4:]}'
            nova_data_vencimento_receita_final=datetime.datetime.strptime(vencimento_da_receita_formatada,"%d/%m/%Y")

            

            dados_receita.pop(receita_que_vai_ser_editada)

            nova_receita=Receita(uuid.uuid4(),novo_nome_receita,novo_valor_receita,nova_descrição_receita,nova_data_vencimento_receita_final)
            
        
            dados_receita.insert(receita_que_vai_ser_editada,nova_receita)
                
            print('Receita editada com sucesso!')

            input('Digite uma tecla para voltar ao menu principal')
                

        except:
            print('ERRO, valor inválido!')
            input('Digite uma tecla para voltar ao menu principal')
            
            
    

