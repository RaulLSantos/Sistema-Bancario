'''
Regra:
3 saques diários no valor máximo de 500 por saque.
Depósito maior que zero
Saque maior que zero
Saque deve ser maior que Saldo
Extrato deve listar dos os depósitos e saques realizados
No fim da listagem deve ser exibido o saldo atual
Os valores devem ser no formato float

Nova Regra: Separar as funcionalidades (Saque, depósito...) em funções e criar duas novas funções: uma para 
cadastrar usuário e outra para cadastrar conta bancária.
A função Saque deve receber os argumentos apenas por nome (keyword only)
A função Depósito deve receber os argumentos apenas por posição
A função Extrato deve receber os argumentos por posição e nome (Argumento posicional: saldo. Argumento nomeado: extrato. )

'''
import os
os.system('cls')

def fun_menu():

    menu = '''
    Menu:

    [1] - Depositar 
    [2] - Sacar
    [3] - Extrato
    [99] - Sair

    => '''
    return menu

def fun_saque(*,saque,saldo,limite,numero_saques,extrato):
    # A função Saque deve receber os argumentos apenas por nome (keyword only)      
    if saque > saldo:
        print("\nSaldo indisponível!")           
    elif saque > limite:
        print("\nValor maior que permitido. Limite por saque R$500.00.")           
    elif saque == 0:
        print("Valor de saque deve ser maior que zero.")      
    elif saque <= saldo and saque > 0:
        numero_saques += 1

        saldo -= saque

        print(f"\n\nSeu saque de R${saque} foi efetuado com sucesso.")

        print(f"\n Função Saque: {numero_saques}")
            
        extrato += f'Saque R${saque:.2f}\n'
    return saldo, extrato, numero_saques
    
def fun_deposito(saldo, extrato,/):
    # A função Depósito deve receber os argumentos apenas por posição
    deposito = float(input("Informe o valor a depositar: R$"))
        
    if deposito > 0:

        saldo += deposito

        print(f"\n\nSeu depósito de R${deposito} foi efetuado com sucesso.")

        extrato += f'Depósito R${deposito:.2f}\n'
    else:
        print("\n\nValor inválido.")
    return saldo, extrato

def fun_extrato(saldo,/,*,extrato):
    # A função Extrato deve receber os argumentos por posição e nome (Argumento posicional: saldo. Argumento nomeado: extrato. )

    print(f"\n\nExtrato: {extrato}\n\nSaldo Atual: R${saldo:.2f}\n\n")
    return saldo, extrato

def main():
    saldo = 0
    limite = 500
    extrato = ""
    LIMITE_SAQUES = 3
    numero_saques = 0
    while True:

        opcao = str(input(fun_menu()))

        if opcao == "1":
        # [1] - Depositar 
            saldo, extrato = fun_deposito(saldo,extrato)    
        elif opcao == "2":
        # [2] - Saque 
            print(f"\n Função Menu: {numero_saques}")
            if numero_saques < LIMITE_SAQUES:
                valor = float(input("Informe o valor que deseja sacar: R$"))

                saldo, extrato, numero_saques = fun_saque(
                    saque = valor,
                    saldo = saldo,
                    limite = limite,
                    numero_saques = numero_saques,
                    extrato = extrato
                )
            else:
                print("\nLimite diário de saques atingido. Máximo de 3 por dia!")
        elif opcao == "3":
        # [3] - Extrato
            saldo, extrato = fun_extrato(saldo, extrato = extrato)   
        elif (opcao.upper()) == "99":
            break
        else: 
            print("Operação inválida. Por favor, selecione novamente a opção desejada.")

main()
