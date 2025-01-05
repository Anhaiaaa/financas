#Cadastrar despesa
#Listar despesas 
#Excluir despesa
#Editar despesa
from dados import lista_despesas, lista_contas
from Despesa import Despesa
import uuid
import os
import datetime
from conta_service import Listar_contas
from menus import menu_editar_despesa

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
        opcao_despesas=str(input('Selecione uma opção:'))
        if opcao_despesas=='1':
            Cadastrar_despesa()
           
        if opcao_despesas=='2':
             Listar_despesas_voltar_menu_principal()

        if opcao_despesas=='3':
             Excluir_despesas()

        if opcao_despesas=='4':
             Editar_despesa()
             
        if opcao_despesas>'4':
            os.system('cls')
            print('ERRO, selecione uma opção válida!')
            input('Digite uma tecla para voltar ao menu principal')
        
             
             
    except ValueError():
            os.system('cls')
            print('Valor inválido, erro na digitação!')
            input('Digite uma tecla para voltar ao menu principal')
        
def Cadastrar_despesa():
    os.system('cls')
    print('-'*28)
    print(' '*4,'CADASTRAR DESPESAS')
    print('-'*28)
    try:
        nome_da_despesa= str(input('Digite o nome da despesa:')).capitalize()
        valor_da_despesa=float(input('Digite o valor da despesa:'))

        descricao_da_despesa=str(input('\nDigite a descrição da despesa:')).capitalize()

        vencimento_da_despesa=input('\nInforme a data de vencimento da receita sem as barras ex:(01012024):')
        vencimento_da_despesa_formatada= f'{vencimento_da_despesa[0:2]}/{vencimento_da_despesa[2:4]}/{vencimento_da_despesa[4:]}'
        vencimento=datetime.datetime.strptime(vencimento_da_despesa_formatada,"%d/%m/%Y")

        os.system('cls')
      
        for conta in lista_contas:
                Listar_contas()
                transferir_despesa_conta=str(input('Deseja transferir a despesa para qual conta?\n(Informe o Nome da conta):'))
                if transferir_despesa_conta==conta.nome:
                    

                    despesa1=Despesa(uuid.uuid4(),nome_da_despesa,valor_da_despesa,descricao_da_despesa,vencimento)
                    lista_despesas.append(despesa1)

                    print('\nDespesa cadastrada com sucesso!')
                    
                
                else:
                    print(f'O nome {transferir_despesa_conta} não esta na lista de contas')
            

    

        
        input('Digite uma tecla para voltar ao menu principal:')

    except ValueError:
         print('ERRO, valor inválido!')
         input('Digite uma tecla para voltar ao menu principal:')

def Listar_despesas():
    os.system('cls')
    print('-'*22)
    print(' '*6,'GASTOS')
    print('-'*22)
    
    for  indicie,despesa_item in enumerate(lista_despesas):
            
            print(f'{indicie+1}-{despesa_item.nome} R$ {despesa_item.valor:.2f}\nDescrição:{despesa_item.descricao}\nValidade:{despesa_item.vencimento}\n')
            
def Listar_despesas_voltar_menu_principal():
     Listar_despesas()
     input('Digite uma tecla para voltar ao menu principal')
     
def Excluir_despesas():
    try:
        Listar_despesas()
        despesa_excluida_pelo_usuario=int(input('Qual despesa deseja excluir?'))
        lista_despesas.pop(despesa_excluida_pelo_usuario-1)
        
        print('\nDespesa excluída com sucesso!')
        input('Digite uma tecla para voltar ao menu principal:')
       
    except ValueError:
        print('Erro, valor inválido!')
        input('Digite uma tecla para voltar ao menu principal:')
        pass

def Editar_despesa():
    
        try:
            Listar_despesas()
            despesa_que_vai_ser_editada=int(input('Qual despesa deseja editar?'))-1
            os.system('cls')
            menu_editar_despesa()
            novo_nome_despesa=str(input('Digite o novo nome da despesa:')).capitalize()
            novo_valor_despesa=float(input('Digite o novo valor da despesa:'))
            nova_descrição_despesa=str(input('\nDigite a descrição da despesa:')).capitalize()
            nova_data_vencimento_despesa=input('\nInforme a data de vencimento da receita sem as barras ex:(01012024):')
            vencimento_da_despesa_formatada= f'{nova_data_vencimento_despesa[0:2]}/{nova_data_vencimento_despesa[2:4]}/{nova_data_vencimento_despesa[4:]}'
            nova_data_vencimento_despesa_final=datetime.datetime.strptime(vencimento_da_despesa_formatada,"%d/%m/%Y")

            
            lista_despesas.pop(despesa_que_vai_ser_editada)

            nova_despesa=Despesa(uuid.uuid4(),novo_nome_despesa,novo_valor_despesa,nova_descrição_despesa,nova_data_vencimento_despesa_final)
            
        
            lista_despesas.insert(despesa_que_vai_ser_editada,nova_despesa)
                
            print('Despesa editada com sucesso!')

            input('Digite uma tecla para voltar ao menu principal')
                

        except:
            print('ERRO, valor inválido!')
            input('Digite uma tecla para voltar ao menu principal')
            
            
    

   