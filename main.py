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


def sacar(*,saldo, valor, extrato, limite):
    
    global numero_de_saques
    global soma_de_saques_diarios
    global contagem
    excedeu_saldo = valor > saldo
    excedeu_limite = valor + soma_de_saques_diarios > limite
    excedeu_saques = numero_de_saques >= LIMITE_SAQUES
    
    if excedeu_saques == False:        
        if excedeu_limite:
            print(f"Você atingiu o limite de R$ {limite:.2f} para saque diários. Você já sacou R$ {soma_de_saques_diarios:.2f} hoje.")
        elif excedeu_saldo: 
            print("Você não tem saldo suficiente para efetuar essa transação.")
        elif valor > 0:
            saldo -= valor
            numero_de_saques += 1
            soma_de_saques_diarios += valor
            contagem += 1
            extrato += f"Saque: \t \t R$ {valor:.2f}\n"
            print(f"Você sacou R$ {valor:.2f} seu saldo atual é R$ {saldo:.2f}")
    else:
        print(f"Você atingiu o limite de {LIMITE_SAQUES} de saques diários")

    return (saldo, extrato)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        global contagem
        contagem += 1
        saldo += valor
        extrato += f"Depósito: \t R$ {valor:.2f}\n"
        print(f"Você depositou R$ {valor:.2f} seu saldo atual é R$ {saldo:.2f}")
    else:
        print("Erro com o valor, tente novamente com valores iguais ou superiores a R$ 1,00.")

    return (saldo, extrato)

def exibir_extrato(saldo,/, *, extrato):
    global contagem
    if contagem == 0:
        print("*************** EXTRATO ***************")
        print("Não foram realizadas transações hoje.")
        print(f"Seu saldo atual é R$ {saldo:.2f}")
        print("======================================")
    elif contagem > 0:
        print("*************** EXTRATO ***************")
        print(extrato)
        print(f"Saldo: \t \t R$ {saldo}")
        print("=======================================")
    return(saldo, extrato)

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Qual o valor que deseja sacar: "))
        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
        )          
  

    elif opcao == "2":
        valor = float(input("Quanto você deseja depositar? "))
        
        saldo, extrato = depositar(
            saldo,
            valor,
            extrato
        )
       
    elif opcao == "3":
        saldo, extrato = exibir_extrato(
            saldo,
            extrato=extrato
        )


    elif opcao == "4":
        break
    else:
        print("Opção inválida, tente novamente com uma opção válida.")


