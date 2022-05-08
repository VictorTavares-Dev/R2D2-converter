import traceback
from app.log.Logger import Logger
from app.user.User import User

logger = Logger()
user = User(logger)

user.get_user_name()

logger.info(f"Nome de usuário = {user.user_name}")
logger.info(f"Iniciando o projeto!")

