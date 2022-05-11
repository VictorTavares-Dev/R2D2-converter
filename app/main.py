import traceback
from app.log.Logger import Logger
from app.user.User import User
from app.converter.Converter import Converter

logger = Logger()
user = User(logger)
converter = Converter()

user.get_user_name()

logger.info(f"Nome de usuario = {user.user_name}")
logger.info(f"Iniciando o projeto!")
logger.info(f"Solicitando opcao de conversao ao usuario")
print(f"Ola, {user.user_name}. O que deseja fazer?")
print("Escolha apenas uma opcao:")
print("1 - Conversao binaria.")
print("2 - Conversao octodecimal.")
print("3 - Conversao hexadecimal.\n")
option = int(input("Opcao: "))

if option == 1:
    logger.info(f"Opcao escolhida [1 - Conversao binaria]")
    print("\nOpcao escolhida: 1 - Conversao binaria")
    print("Otimo! Por favor, digite um numero decimal inteiro para a conversao\n")
    logger.info(f"Solicitando numero decimal ao usuario para conversao")
    decimal = int(input("Numero: "))

    converter.decimal = decimal
    logger.info(f"Numero informado: {decimal}")
    logger.info(f"Convertendo o numero {decimal} para a base binaria")
    print("\nConvertendo numero para binario...")
    binary = converter.to_binary()
    logger.info(f"Conversao realizada com sucesso. Numero resultante: {binary}")
    print(f"RESULTADO: {binary}")

