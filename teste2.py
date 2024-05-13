lista_equipamentos = ""

# TODO: Crie um loop para solicita os itens ao usuário:

# TODO: Solicite o item e armazena na variável "item":

# TODO: Adicione o item à lista "itens":
for i in range(3):
  item = input()
  lista_equipamentos.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in lista_equipamentos:
    
    print(f"- {item}")