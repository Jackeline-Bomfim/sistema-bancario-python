def cadastrar_equipamentos():
    # Cria uma lista vazia para armazenar os equipamentos
    lista_equipamentos = []

    # Loop para solicitar ao usuário inserir até três equipamentos
    for i in range(3):
        equipamento = input(f"Informe o nome do {i+1}º equipamento: ")
        lista_equipamentos.append(equipamento)

    # Exibe a lista de equipamentos cadastrados
    print("\nEquipamentos cadastrados:")
    for equipamento in lista_equipamentos:
        print(f"- {equipamento}")

# Chama a função para cadastrar os equipamentos
cadastrar_equipamentos()
