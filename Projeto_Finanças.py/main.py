from time import sleep
import os
from despesas_service import Menu_Despesas
from receita_service import Menu_Receita
from conta_service import Menu_Conta
from menus import Menu_Principal


print('-'*22)
print(' '*5,'FINANÇAS')
print('-'*22)
print('Seja bem vindo ao nosso sistema de controle financeiro!')
sleep(2.5)
while True:
    try:
        Menu_Principal()
        opcao=int(input('Selecione uma opção:'))
    
        if opcao==1:
            Menu_Despesas()
            
        if opcao==2:
            Menu_Receita()
            
        if opcao==3:
            Menu_Conta()

        if opcao==4:
            os.system('cls')
            print('Encerrando programa...')
            sleep(2)
            os.system('cls')
            break
        
        if opcao>4:
            os.system('cls')
            print('ERRO, selecione uma opção válida!')
            input('Digite uma tecla pra voltar ao menu principal')

    except ValueError:
         os.system('cls')
         print('ERRO, selecione uma opção válida!')
         input('Digite uma tecla para voltar ao menu principal:')

   
           

    



