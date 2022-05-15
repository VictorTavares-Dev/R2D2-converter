import traceback
from app.log.Logger import Logger
from app.user.User import User
from app.converter.Converter import Converter
from app.console.Console import Console

try:
    logger = Logger()

    logger.info("Iniciando aplicacao R2D2 Numeric Base Converter")
    user = User(logger)
    converter = Converter(logger)
    console = Console(user, logger, converter)

    console.welcome_message()

    logger.info("Execucao finalizada com sucesso")

except Exception:
    logger.error("Execucao finalizada com erro", traceback.format_exc())
