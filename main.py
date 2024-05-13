import textwrap

menu = """
====================
 [1] Sacar
 [2] Depositar
 [3] Extrato
 [4] Cadastro de usuário  
 [5] Criar uma nova conta 
 [6] Listar contas
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
usuarios = []
contas = []
AGENCIA = "0001"


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

def cadastro_usuário(usuarios):
    cpf = input("Informe seu CPF(somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso")
        return {"agencia":agencia,"numero_conta":numero_conta, "usuario": usuario}
               
    print("\nUsuário não encontrado, conta não pode ser criada.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


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
        cadastro_usuário(usuarios)

    
    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)


    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "0":
        break

    else:
        print("Opção inválida, tente novamente com uma opção válida.")


