import traceback
from app.log.Logger import Logger


class User:
    """
    A class to represent a user.

    Attributes
    ----------
    user_name : str
        first name of the user.

    Methods
    -------
    get_user_name():
        Gets the user's name.
    """

    def __init__(self, logger: Logger, user_name=None):
        """
        Constructs all the necessary attributes for the user object.

        Parameters
        ----------
            user_name : str
                first name of the user.
            logger : Logger
                logger for logging purposes.
        """
        self.user_name = user_name
        self.logger = logger

    def get_user_name(self):
        """
        Gets user's first name from input on console/terminal. Sets the name in the variable user_name of the class User.

        Parameters
        ----------
            None.

        Returns
        -------
            None.
        """
        try:
            self.logger.info("Recuperando nome de usuario da entrada via console.")
            name = str(input("Por favor, insira o seu primeiro nome: "))

            # Checks if name is empty
            while not (len(name) >= 2 and name.isalpha()):
                self.logger.info(f"Nome recuperado com sucesso. Nome inserido: {name}")
                self.logger.warn("Nome de usuario deve ser maior do que uma letra e nao pode conter numeros, simbolos"
                                 " ou espacos!")

                print("ERRO: Nome de usuário deve ser maior do que uma letra e nao pode conter numeros, simbolos ou "
                      "espacos!")
                self.logger.info("Solicitando nova entrada de nome do usuario.")

                name = str(input("Por favor, insira o seu primeiro nome: "))
            else:
                self.user_name = name
                print(f"\nOla, {self.user_name}. O que deseja fazer?")
                self.logger.info(f"Nome recuperado com sucesso. Nome inserido: {self.user_name}")

        except Exception as e:
            self.logger.error("Falha na recuperação de nome do usuário.", traceback.format_exc())
