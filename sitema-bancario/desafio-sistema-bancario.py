menu = """
        => 
            [D] Depositar
            [S] Sacar
            [E] Extrato
            [Q] Sair
        =>
"""
texto_extrato = "EXTRATO"
fim_extrato = "="
saldo = 0
extrato = ""
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3

while True:
    opcao = input(menu.center(15))

    if opcao == "D" or opcao == "d":
        print("Opção selecionada: Depósito")
        valor_deposito = float(input("Quanto você deseja depositar? "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: {valor_deposito:.2f}\n"
        else:
            print("Operação falhou. Tente novamente.")

    elif opcao == "S" or opcao == "s":
        print("Opção selecionada: Saque")
        valor_saque = float(input("Quanto você deseja sacar?"))
        if valor_saque > LIMITE:
            print("Não foi possível continuar o seu saque. Valor excede o permitido por saque!")
        elif valor_saque > saldo:
            print("Não foi possível continuar o seu saque. Valor excede o saldo da conta!")
        elif numero_saques >= 3:
            print("Não foi possível continuar o seu saque. Quantidade de saques diários excedida!")
        else:
            print("Sucesso! Retire seu dinheiro.")
            saldo -= valor_saque
            extrato += f"Saque: {valor_saque:.2f}\n"
            numero_saques += 1

    elif opcao == "E" or opcao == "e":
        print("Opção selecionado: Extrato")
        print(texto_extrato.center(35,"="))
        print("Não foram realizadas movimentações na conta!" if not extrato else extrato)
        print(f"Saldo: {saldo:.2f}")
        print(fim_extrato.center(35,"="))
    elif opcao == "Q" or opcao == "q":
        print("Ok, saindo do sistema!")
        break
    else:
        print("Opção inválida! Selecione uma das opções.")
