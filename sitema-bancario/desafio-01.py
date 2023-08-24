# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("=" * 15)
    print("[D] Depositar")
    print("[S] Sacar")
    print("[E] Extrato")
    print("[Q] Sair")
    print("=" * 15)

# Inicialização das variáveis
saldo = 0
extrato = []
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip().lower()

    if opcao == "d":
        valor_deposito = float(input("Quanto você deseja depositar? "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(f"Depósito: {valor_deposito:.2f}")
        else:
            print("Operação falhou. Tente novamente.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Não foi possível continuar o seu saque. Quantidade de saques diários excedida!")
        else:
            valor_saque = float(input("Quanto você deseja sacar? "))
            if valor_saque > LIMITE:
                print("Não foi possível continuar o seu saque. Valor excede o permitido por saque!")
            elif valor_saque > saldo:
                print("Não foi possível continuar o seu saque. Valor excede o saldo da conta!")
            else:
                saldo -= valor_saque
                extrato.append(f"Saque: {valor_saque:.2f}")
                numero_saques += 1
                print("Sucesso! Retire seu dinheiro.")

    elif opcao == "e":
        print("=" * 35)
        print("EXTRATO".center(35))
        for transacao in extrato:
            print(transacao)
        print("=" * 35)
        print(f"Saldo: {saldo:.2f}")
    elif opcao == "q":
        print("Ok, saindo do sistema!")
        break
    else:
        print("Opção inválida! Selecione uma das opções.")
