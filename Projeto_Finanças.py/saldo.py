
from dados import despesas,dados_receita
import os

def mostrar_saldo():
    os.system('cls')
    print('-'*22)
    print(' '*5,'SALDO')
    print('-'*22)
    saldo=0

    for despesa_item in despesas:
        saldo = saldo - despesa_item.valor
        print(f'R$-{saldo:.2f}')
    
    for receita_item in dados_receita:
        saldo = saldo + receita_item.valor
        print(f'R$-{saldo:.2f}')

    print(f'FINAL-{saldo:.2f}')
    input('Digite uma tecla para voltar ao menu principal:')
    
    
       