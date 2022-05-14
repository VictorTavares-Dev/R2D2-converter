from app.user.User import User
from app.log.Logger import Logger
from app.converter.Converter import Converter
from prettytable import PrettyTable


class Console:
    """
    A class to represent a console application to get sn show info to the user.

    Attributes
    ----------
    user: User
        the user class of the application.
    logger: Logger
        the logger class of the application.
    converter: Converter
        the converter class of the application.
    option: str
        the main menu option retrieved from user input.
    list_of_options: List
        a list tha represent the actual option value based on the number retrieved from user input.
    new_option: str
        the new option retrieved from user input at continue menu.
    results_list: List
        the list of converted numbers based on user input.

    Methods
    -------
    welcome_message(): void
        method to print a welcome message for the user and retrieve user's name.
    main_menu(): void
        method to print main menu options and get input from the user.
    validate_main_menu_option(): void
        method to validate the main menu option chosen by the user.
    get_decimal_number(): void
        method to ask decimal number for conversion from user's input.
    print_result(): void
        method to print the result of a conversion on the screen for the user.
    output_formatter(): void
        method to format the result of conversions into results_list variable.
    conversion_job(): void
        method to execute conversion of a decimal number retrieved from user's input to the numeric base chosen by said
        user.
    continue_menu(): void
        method to print a new menu based on the option chosen by the user, asking for a new option entry.
    validate_continue_options(): void
        method to validate option chosen by the user retrieved from continue_menu(). Depending on the option chosen by
        the user, this method is responsible to end the application.
    """
    def __init__(self, user: User, logger: Logger, converter: Converter, option=None, new_option=None,
                 results_list=None):
        if results_list is None:
            results_list = []
        self.user = user
        self.logger = logger
        self.converter = converter
        self.option = option
        self.list_of_options = ["1 - Conversao binaria", "2 - Conversao octodecimal", "3 - Conversao hexadecimal"]
        self.new_option = new_option
        self.results_list = results_list

    def welcome_message(self):
        """
        Prints a welcome message for the user and retrieves user's name. After retrieving user's name properly, invokes
        main_menu() method.

        Parameters
        ----------
            None.

        Returns
        -------
            None.
        """
        self.logger.info("Exibindo mensagem de boas-vindas")

        print("╔═══════════════════════════════════════════════════════════════════════════════════════╗")
        print("║\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t║")
        print("║\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t║")
        print("║\t\t\t\t\t\tBem-vinde ao R2D2 Numeric Base Converter!\t\t\t\t\t\t║")
        print("║\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t║")
        print("║\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t║")
        print("╚═══════════════════════════════════════════════════════════════════════════════════════╝")

        self.user.get_user_name()
        self.main_menu()

    def main_menu(self):
        """
        Prints main menu options and gets input from the user. Validates the input via validate_main_menu_option()
        method and invokes conversion_job() method.

        Parameters
        ----------
            None.

        Returns
        -------
            None.
        """
        self.logger.info("Solicitando entrada do usuario para opcao de conversao numerica")

        print("\nEscolha apenas uma opcao:")

        for item in self.list_of_options:
            print(item)

        self.option = str(input("\nOpcao escolhida: "))

        self.logger.info(f"Opcao recuperada: {self.option}")
        self.validate_main_menu_option()

        self.logger.info(f"Opcao escolhida: {self.list_of_options[int(self.option) - 1]}")

        self.conversion_job()

    def validate_main_menu_option(self):
        """
        Validates the main menu option chosen by the user and ask new entry until option is valid.

        Parameters
        ----------
            None.

        Returns
        -------
            None.
        """
        while self.option not in ["1", "2", "3"]:
            self.logger.warn("Opcao invalida. Solicitando nova entrada para o usuario")

            print("ERRO: Por favor, insira uma opcao valida")
            self.option = str(input("Opcao escolhida: "))

            self.logger.info(f"Opcao recuperada: {self.option}")

    def get_decimal_number(self):
        """
        Retrieves decimal number for conversion from user's input. While the content retrieved is not a decimal number,
        keeps asking for a new input.

        Parameters
        ----------
            None.

        Returns
        -------
            None.
        """
        self.converter.decimal = input("Numero: ")

        self.logger.info(f"Numero recuperado : {self.converter.decimal}")

        while not self.converter.decimal.isdigit():
            self.logger.warn("Conteudo recuperado nao eh um numero decimal inteiro")
            self.logger.info("Solicitando nova entrada para o usuario")
            print("\nERRO: Por favor, insira um numero decimal inteiro valido.")
            self.converter.decimal = input("Numero: ")
        else:
            self.logger.info("Numero decimal recuperado com sucesso")
            self.converter.decimal = int(self.converter.decimal)

    def print_result(self):
        """
        Prints the result of a numeric base conversion on the screen for the user. Invokes output_formatter() method
        to format results into results_list variable.

        Parameters
        ----------
            None.

        Returns
        -------
            None.
        """
        self.logger.info("Imprimindo resultado da conversao para o usuario")

        if self.option == "1":
            result = self.converter.binary
        elif self.option == "2":
            result = self.converter.octal
        elif self.option == "3":
            result = self.converter.hexal

        print("╔", end="")
        for item in range(0, len(result) + 16):
            print("═", end="")
        print("╗")
        print("║  ", end="")
        print(f"RESULTADO: {result}", end="   ║\n")
        print("╚", end="")
        for item in range(0, len(result) + 16):
            print("═", end="")
        print("╝")

        self.logger.info("Resultado impresso com sucesso")

        self.output_formatter()

    def output_formatter(self):
        """
        Formats the result of conversions into results_list variable to be used to print a table of conversions
        made during the use of the application

        Parameters
        ----------
            None.

        Returns
        -------
            None.
        """
        self.logger.info("Iniciando processo de formatacao de resposta para tabela final")

        if self.option == "1":
            base = "Binario"
            conversion_result = str(self.converter.binary)
        elif self.option == "2":
            base = "Octodecimal"
            conversion_result = str(self.converter.octal)
        elif self.option == "3":
            base = "Hexadecimal"
            conversion_result = str(self.converter.hexal)

        formatted_result = [self.converter.decimal, base, conversion_result]
        self.results_list.append(formatted_result)

        self.logger.info("Formatacao de linha para tabela realizada com sucesso")

    def conversion_job(self):
        """
        Execute conversion of a decimal number retrieved from user's input to the numeric base chosen by said
        user. When conversion is succeeded, invokes print_result() and continue_menu() methods.

        Parameters
        ----------
            None.

        Returns
        -------
            None.
        """
        print(f"\nOpcao escolhida: {self.list_of_options[int(self.option) - 1]}")

        self.logger.info("Solicitando numero decimal para conversao")
        print("Otimo! Por favor, digite um numero decimal inteiro para a conversao\n")
        self.get_decimal_number()

        if self.option == "1":
            print("\nConvertendo numero para binario...")
            self.converter.binary = self.converter.to_binary()

        elif self.option == "2":
            print("\nConvertendo numero para base octodecimal...")
            self.converter.octal = self.converter.to_octodecimal()

        elif self.option == "3":
            print("\nConvertendo numero para base hexadecimal...")
            self.converter.hexal = self.converter.to_hexadecimal()

        self.print_result()
        self.continue_menu()

    def continue_menu(self):
        """
        Prints a new menu based on the option chosen by the user, asking for a new option entry. Invokes
        validate_continue_menu_option() method for entry validation.

        Parameters
        ----------
            None.

        Returns
        -------
            None.
        """
        print("\n#########################################################################################\n")

        self.logger.info("Solicitando escolha de nova opcao para o usuario")

        print(f"Fim da conversao. O que deseja fazer, {self.user.user_name}?")
        if self.option == "1":
            print(f"1 - Converter outro numero para base binaria")
        elif self.option == "2":
            print(f"1 - Converter outro numero para base octodecimal")
        elif self.option == "3":
            print(f"1 - Converter outro numero para base hexadecimal")

        print("2 - Voltar ao menu inicial")
        print("3 - Encerrar aplicacao\n")
        self.new_option = str(input("Opcao escolhida: "))

        self.logger.info(f"Opcao recuperada: {self.new_option}")

        self.validate_continue_options()

    def validate_continue_options(self):
        """
        Validates option chosen by the user retrieved from continue_menu() and treats action:

        Option      Action
        -------     ------
            1       invokes conversion_job() method to ask for a new number for numeric base conversion on base
                    previously chosen by the user.

            2       invokes main_menu() method to ask for a new option input of a numeric base conversion to the user.

            3       ends the application by printing goodbye message and prints a list of conversions the user has
                    made during the use of the app.

        Parameters
        ----------
            None.

        Returns
        -------
            None.
        """
        while self.new_option not in ["1", "2", "3"]:
            self.logger.warn("Opcao invalida. Solicitando nova entrada para o usuario")

            print("ERRO: Por favor, insira uma opcao valida")
            self.option = str(input("Opcao escolhida: "))

            self.logger.info(f"Opcao recuperada: {self.option}")

        if self.new_option == "1":
            self.logger.info(f"Iniciando novo processo de conversao numerica. Opcao escolhida: {self.new_option}")
            self.conversion_job()
        elif self.new_option == "2":
            self.main_menu()
        else:
            self.logger.info("Encerrando aplicacao")
            print(f"\nObrigado por escolher a R2D2 Numeric Base Converter, {self.user.user_name}!")
            print("Abaixo, segue uma relação dos numeros que voce converteu:\n")
            self.logger.info(f"Lista de conversoes realizadas:")

            table = PrettyTable(['NUMERO DECIMAL', 'BASE CONVERTIDA', 'RESULTADO'])
            for item in self.results_list:
                table.add_row(item)

            self.logger.info(f"\n{table}")

            print(table)
