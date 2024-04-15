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

while True:

    opcao = input(menu)

    if opcao == "1":

        if numero_de_saques < LIMITE_SAQUES:
            valor = float(input("Quanto você deseja sacar? "))

            if valor <= saldo and valor <= 500:
                contagem += 1
                saldo -= valor
                numero_de_saques =+ 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(f"Você sacou R$ {valor:.2f} seu saldo atual é R$ {saldo:.2f}")
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


    elif opcao == "4":
        break
    else:
        print("Opção inválida, tente novamente com uma opção válida.")


