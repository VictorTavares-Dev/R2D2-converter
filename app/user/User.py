
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

    def __init__(self, user_name=None):
        """
        Constructs all the necessary attributes for the user object.

        Parameters
        ----------
            user_name : str
                first name of the user.
        """
        self.user_name = user_name

    def get_user_name(self):
        """
        Gets user's first name from input on console/terminal. Records the name in a variable of the class User.

        Parameters
        ----------
            None.

        Returns
        -------
            self.user_name : string
                First name provided by the user and recorded in an instance of the class.
        """
        try:
            name = str(input("Por favor, insira o seu primeiro nome: "))

            # Checks if name is empty
            while not (len(name) >= 2 and name.isalpha()):
                print("Erro! Nome de usuário deve ser maior do que uma letra e nao pode conter numeros, simbolos ou "
                      "espacos!")
                name = str(input("Por favor, insira o seu primeiro nome: "))
            else:
                self.user_name = name

            return self.user_name

        except BaseException() as e:
            print(e)
