import textwrap

def menu():
    TEXTO_INICIO_MENU = "==========Menu=========="
    TEXTO_FIM_MENU = "========================"
    menu = f"""
    {TEXTO_INICIO_MENU}
    [D] \tDepositar
    [S] \tSacar
    [E] \tVerificar Extrato 
    [CU] \tCadastrar usuário
    [CC] \tCadastrar conta
    [LC] \tListar contas
    {TEXTO_FIM_MENU}             
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor,extrato,/):
    if valor > 0:
        extrato += f"Depósito:\t R${valor:.2f}\n"
        saldo += valor
        print("Depósito realizado com sucesso!")
    else: print("Operação inválida! Não é possível deposítar um valor inferior a 0")
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite_saques, limite, numero_saques):
    if valor > limite:
        print("O valor ultrapassa o limite por saques!")
    elif numero_saques >= limite_saques: print("Numeros de saques diários excedidos!")
    elif saldo < valor: print("O valor informado ultrapassa o saldo da conta!")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque:\t R${valor:.2f}\n"
        print(f"Pronto, pode sacar o seu dinheiro: R$ {valor:.2f}")
    else: print("Operação falhou. Valor informado inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo,/,*,extrato):
    print("==========Extrato==========")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("===========================")
    
def criar_usuarios(usuarios):
    cpf = input("Digite o CPF: (Somente os números)")
    usuario = consulta_usuario(cpf, usuarios)
    if usuario:
        print("Usuário já cadastrado com este CPF!")
        return 
    nome = input("Nome completo:")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (Logradouro, nº - Bairro - Cidade/Sigla Estado):" )
    usuarios.append({"cpf":cpf,"nome":nome, "data_nascimento":data_nascimento, "endereco":endereco})  
    print("Usuário criado com sucesso!")
    
def consulta_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF do usuário: ")
    usuario = consulta_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    
def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    LIMITE = 500
    contas = []
    usuarios = []
    numero_saques = 0
    extrato = ''
    saldo = 0
    while True:
        opcao = menu()        
        if opcao == "d" or opcao == "D":
            valor_deposito = float(input("Informe o valor a ser depositado:"))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)
        elif opcao == "s" or opcao == "s":
            valor_saque = float(input("Informe o valor a ser sacado:"))
            saldo, extrato, numero_saques = sacar(saldo=saldo,valor=valor_saque,extrato=extrato,limite_saques=LIMITE_SAQUES,limite=LIMITE,numero_saques=numero_saques)
        elif opcao == "e" or opcao == "E": exibir_extrato(saldo, extrato=extrato)
        elif opcao == "cu" or opcao == "CU":  criar_usuarios(usuarios)
        elif opcao == "cc" or opcao == "CC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta: contas.append(conta)
        elif opcao == "lc" or opcao == "LC": listar_contas(contas)
        elif opcao == "q" or opcao == "Q":  break
        else:  print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
