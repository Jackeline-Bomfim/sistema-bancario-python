import re

def validar_numero_telefone(numero: str) -> bool:
    """
    Valida se um número de telefone está no formato correto.

    Args:
        numero (str): Número de telefone a ser validado.

    Returns:
        bool: True se o número estiver no formato correto, False caso contrário.
    """
   
    padrao = r"\(\d{2}\) 9\d{4}-\d{4}"


    return bool(re.match(padrao, numero))

numero_cliente = input("Informe o número de telefone: ")
if validar_numero_telefone(numero_cliente):
    print("Número válido!")
else:
    print("Número inválido. O formato correto é (XX) 9XXXX-XXXX.")
