from time import sleep
import os
from despesas_service import Menu_Despesas
from receita_service import Menu_Receita
from conta_service import Menu_Conta
from menus import Menu_Principal
from saldo import mostrar_saldo

print('-'*22)
print(' '*5,'FINANÇAS')
print('-'*22)
print('Seja bem vindo ao nosso sistema de controle financeiro!')
sleep(2.5)
while True:
    try:
        Menu_Principal()
        opcao=int(input('Selecione uma opção:'))
        pass
        if opcao==1:
            Menu_Despesas()
            
        if opcao==2:
            Menu_Receita()
            
        if opcao==3:
            Menu_Conta()
            
        if opcao==4:
            mostrar_saldo()
            
        if opcao==5:
            os.system('cls')
            print('Encerrando programa...')
            sleep(2)
            os.system('cls')
            break
            
        if opcao>5:
            os.system('cls')
            print('ERRO')
            input('Digite uma tecla pra voltar ao menu principal')

    except:
        os.system('cls')
        print('ERRO')
        input('Digite uma tecla pra voltar ao menu principal')
        
           

    



