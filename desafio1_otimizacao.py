import textwrap

def menu():
    menu = """\n
    𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑 MENU 𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑    
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListas Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print('\n𓃑𓃑𓃑𓃑 Depósito realizado com sucesso! 𓃑𓃑𓃑𓃑')
    else:
        print('\n︾︾︾︾ Operação falhou! O valor informado não é válido. ︾︾︾︾')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\n︾︾︾︾ Operação falhou! Você não tem saldo suficiente. ︾︾︾︾')

    elif excedeu_limite:
        print('\n︾︾︾︾ Operação falhou! O valor do saque excede o limite. ︾︾︾︾')

    elif excedeu_saques:
        print('\n︾︾︾︾ Operação falhou! Número máximo de saques excedido. ︾︾︾︾')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n𓃑𓃑𓃑𓃑 Saque realizado com sucesso! 𓃑𓃑𓃑𓃑')

    else:
        print('\n︾︾︾︾ Operação falhou! O valor informado é inválido. ︾︾︾︾')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑 EXTRATO 𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑𓃑')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n︾︾︾︾ Já existe um usuário com este CPF! ︾︾︾︾')
        return
    
    nome = input('Informe o nome Completo: ')
    data_nascimento = input('Informe a data de nascimento: ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('𓃑𓃑𓃑 Usuário cadastrado com sucesso! 𓃑𓃑𓃑')

def filtrar_usuario(cpf, usuarios):
     for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
     return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input ('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n𓃑𓃑𓃑 Conta criada com sucesso! 𓃑𓃑𓃑')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('\n︾︾︾︾ Usuário não encontrado, fluxo de criação de conta encerrado! ︾︾︾︾')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 2500
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar (saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao =='lc':
            listar_contas(contas)

        elif opcao == 'q':
            break
        
        else:
            print('Operação inválida, porfavor selecione novamente a operação desejada.')

main()