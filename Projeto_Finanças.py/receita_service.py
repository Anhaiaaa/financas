#Cadastrar receita
#Listar receitas 
#Excluir receita
#Editar receita
import os
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
    except ValueError():
        print('ERRO')
        print(input('Digite uma tecla para voltar ao menu principal'))

def Cadastrar_receita():
    pass


def Listar_receitas():
    pass

def Excluir_receita():
    pass

def Editar_receita():
    pass

