import traceback
from app.log.Logger import Logger
from app.user.User import User
from app.converter.Converter import Converter
from app.console.Console import Console, welcome_message

logger = Logger()
user = User(logger)
converter = Converter(logger)
console = Console(user, logger, converter)

welcome_message()
user.get_user_name()
console.main_menu()

logger.info(f"Nome de usuario = {user.user_name}")
logger.info(f"Iniciando o projeto!")
logger.info(f"Solicitando opcao de conversao ao usuario")


"""
if option == 1:
    logger.info(f"Opcao escolhida [1 - Conversao binaria]")
    print("\nOpcao escolhida: 1 - Conversao binaria")
    print("Otimo! Por favor, digite um numero decimal inteiro para a conversao\n")
    logger.info(f"Solicitando numero decimal ao usuario para conversao")
    decimal = int(input("Numero: "))

    converter.decimal = decimal
    logger.info(f"Numero informado: {decimal}")
    print("\nConvertendo numero para binario...")
    binary = converter.to_binary()
    print(f"RESULTADO: {binary}")
"""
