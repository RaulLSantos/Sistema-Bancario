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

Função cadastrar usuário:
Deve armazenar o usuário em uma lista composto por: nome, data de nascimento, cpf e endereço
O endereço é uma string com o formato: logradouro, número, bairro, cidade/estado. 
Deve ser armazenado apenas os números do CPF.
Não pode cadastrar dois usuário com o mesmo CPF.

Função Conta Corrente:
Deve armazenar as contas em uma lista. A conta deve ser composta por: agência, número da conta e usuário. 
O número da conta é sequencial, iniciando em 1. O número da agência é fixo: 0001. O usuário pode ter mais de uma conta, 
mas uma conta pertence a somente um usuário.

'''
import os
os.system('cls')

def fun_menu():

    menu = '''
    Menu:

    [1] - Depositar 
    [2] - Sacar
    [3] - Extrato
    [4] - Cadastrar Usuário
    [5] - Criar Conta
    [6] - Listar Contas
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

def fun_cadastro_usuario(usuarios):
    cadastra_cpf = input(str("Digite seu CPF: "))
    usuario = fun_valida_cpf(cadastra_cpf,usuarios)

    if usuario:
        print("!!!! Já exite usuário cadastrado para este CPF !!!!")
        return
    
    nome = input(str("Digite o nome completo: "))
    dt_nascimento = input(str("Digite a data de nascimento: "))
    endereco = input(str("Digite o endereço: (Logradouro, nro - Bairro - Cidade/Estado): "))

    usuarios.append({"nome": nome, "data_nascimento": dt_nascimento, "CPF": cadastra_cpf, "endereço": endereco})

    print(f"\n\n Usuário cadastrado com sucesso!\nNome: {nome}\nData de Nascimento: {dt_nascimento}\nCPF: {cadastra_cpf}\nEndereço: {endereco}" )

def fun_valida_cpf(cadastra_cpf, usuarios):
    # o código que é passado para a variável "usuarios_filtrados" é chamado compressão de listas
    ''' Explicação:
    A partir do IF o código verifica se na chave "CPF" dentro da lista de usuários 
    (in usuarios if usuario["CPF"] == cadastra_cpf) possui um CPF igual ao informado na nova variável
    Se o CPF for igual, vai retornar o usuário e guardar na variável usuarios_filtrados
    '''
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cadastra_cpf]

    ''' Explicação:
    Retorna a variável com índice zero se tiver conteúdo (isso pois o código sempre vai encontrar um único usuário.
    Não pode haver mais de um usuário). Se não encontrar usuário, retorna None
    '''

    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def fun_cadastro_conta_bancaria(AGENCIA,sequencia_conta,usuarios,contas_bancarias):
    # agência, número da conta e usuário.
    cpf = input(str("Digite o CPF para cadastrar a conta: "))
    usuario = fun_valida_cpf(cpf,usuarios) 
    if usuario:
        print(f"\n\nConta cadastrada com sucesso!" )
        contas_bancarias.append({"agencia": AGENCIA, "numero_conta": sequencia_conta, "usuario": usuarios})
        sequencia_conta += 1
        return sequencia_conta
    print(" !!! Usuário não encontrado !!!")
    return sequencia_conta

    

def main():
    AGENCIA = "001"
    sequencia_conta = 1
    contas_bancarias = []
    usuarios = []
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
        elif opcao == "4":
        # [4] - Cadastrar Usuário
            fun_cadastro_usuario(usuarios)
        elif opcao == "5":
        # [5] - Criar Conta
            sequencia_conta = fun_cadastro_conta_bancaria(AGENCIA,sequencia_conta,usuarios,contas_bancarias)

        elif opcao == "6":
        # [6] - Listar Contas
            print(*contas_bancarias)

        elif (opcao.upper()) == "99":
            break
        else: 
            print("Operação inválida. Por favor, selecione novamente a opção desejada.")

main()
