menu = """
====================
 [1] Sacar
 [2] Depositar
 [3] Extrato
 [0] Sair
====================
=>  """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3
contagem = 0
soma_de_saques_diarios = 0

while True:

    opcao = input(menu)

    if opcao == "1":

        if numero_de_saques < LIMITE_SAQUES:
            valor = float(input("Quanto você deseja sacar? "))

            controlador_de_limite = valor + soma_de_saques_diarios

            if valor <= saldo and valor <= limite and controlador_de_limite <= limite:
                contagem += 1
                saldo -= valor
                numero_de_saques +=  1
                soma_de_saques_diarios += valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(f"Você sacou R$ {valor:.2f} seu saldo atual é R$ {saldo:.2f}")
            elif valor > limite:
                print(f"O valor solicitado é maior que o ilimite diário para saque. Atualmente seu limite diário é de {limite:.2f}")
            elif controlador_de_limite >= limite:
                print(f"Você atingiu o limite de R$ {limite:.2f} para saque diários. Você já sacou R$ {soma_de_saques_diarios:.2f} hoje.")
            else: 
                print("Você não tem saldo suficiente para efetuar essa transação.")
        else:
            print("Você atingiu o limite de 3 saques diários.")    

       

    elif opcao == "2":
        valor = float(input("Quanto você deseja depositar? "))
        if valor > 0:
            contagem += 1
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Você depositou R$ {valor:.2f} seu saldo atual é R$ {saldo:.2f}")
        else:
            print("Erro com o valor, tente novamente com valores iguais ou superiores a R$ 1,00.")

       
    elif opcao == "3":
        if contagem == 0:
            print("*************** EXTRATO ***************")
            print("Não foram realizadas transações hoje.")
            print(f"Seu saldo atual é R$ {saldo:.2f}")
            print("======================================")
        elif contagem > 0:
            print("*************** EXTRATO ***************")
            print(extrato)
            print("=======================================")


    elif opcao == "0":
        break
    else:
        print("Opção inválida, tente novamente com uma opção válida.")
