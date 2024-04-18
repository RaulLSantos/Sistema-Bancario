'''
Regra:
3 saques diários no valor máximo de 500 por saque.
Depósito maior que zero
Saque maior que zero
Saque deve ser maior que Saldo
Extrato deve listar dos os depósitos e saques realizados
No fim da listagem deve ser exibido o saldo atual
Os valores devem ser no formato float
'''
import os
os.system('cls')

menu = '''
Menu:

[1] - Depositar 
[2] - Sacar
[3] - Extrato
[S] - Sair

=> '''


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3    



while True:
    
    opcao = str(input(menu))

    mensagem_retorno = '''

    Deseja efetuar outra operação?
    [1] - Sim
    [2] - Não
    => '''

    if opcao == "1":
    # [1] - Depositar 
        
        deposito = float(input("Informe o valor a depositar: R$"))
        
        if deposito > 0:

            saldo += deposito

            print(f"\n\nSeu depósito de R${deposito} foi efetuado com sucesso.")

            extrato += f'Depósito R${deposito:.2f}\n'
            

        else:
            print("\n\nValor inválido.")
                
        

    elif opcao == "2":
    # [2] - Sacar

        
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Informe o valor que deseja sacar: R$"))
            
            if saque > saldo:
                print("\nSaldo indisponível!")
            
            elif saque > limite:
                print("\nValor maior que permitido. Limite por saque R$500.00.")
            
            elif saque == 0:
                print("Valor de saque deve ser maior que zero.")
        
            elif saque <= saldo and saque > 0:
                numero_saques += 1
                print(numero_saques)

                saldo -= saque

                print(f"\n\nSeu saque de R${saque} foi efetuado com sucesso.")
            
                extrato += f'Saque R${saque:.2f}\n'
        else:
            print("\nLimite diário de saques atingido. Máximo de 3 por dia!")
        
       
    
    elif opcao == "3":
    # [3] - Extrato
        
        print(f"\n\nExtrato: {extrato}\n\nSaldo Atual: R${saldo:.2f}\n\n")
        

    elif (opcao.upper()) == "S":
        break
    
    else: 
        print("Operação inválida. Por favor, selecione novamente a opção desejada.")
