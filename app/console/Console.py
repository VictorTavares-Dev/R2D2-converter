from app.user.User import User
from app.log.Logger import Logger
from app.converter.Converter import Converter
from tabulate import tabulate


def welcome_message():
    print("╔═══════════════════════════════════════════════════════════════════════════════════════╗")
    print("║\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t║")
    print("║\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t║")
    print("║\t\t\t\t\t\tBem-vinde ao R2D2 Numeric Base Converter!\t\t\t\t\t\t║")
    print("║\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t║")
    print("║\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t║")
    print("╚═══════════════════════════════════════════════════════════════════════════════════════╝")


class Console:
    def __init__(self, user: User, logger: Logger, converter: Converter, option=None, new_option=None, decimals_list=[],
                 results_list=[]):
        self.user = user
        self.logger = logger
        self.converter = converter
        self.option = option
        self.new_option = new_option
        self.decimals_list = decimals_list
        self.results_list = results_list

    def main_menu(self):
        print("Escolha apenas uma opcao:")
        print("1 - Conversao binaria.")
        print("2 - Conversao octodecimal.")
        print("3 - Conversao hexadecimal.\n")

        self.option = str(input("Opcao: "))
        self.validate_option()
        self.main_menu_options()

    def validate_option(self):

        while self.option not in ["1", "2", "3", "4", "5"]:
            print("ERRO: Por favor, insira uma opcao valida")
            self.option = str(input("Opcao escolhida: "))

    def get_decimal_number(self):
        self.converter.decimal = input("Numero: ")

        while not self.converter.decimal.isdigit():
            print("\nERRO: Por favor, insira um numero decimal inteiro valido.")
            self.converter.decimal = input("Numero: ")
        else:
            self.converter.decimal = int(self.converter.decimal)

    def print_result(self):

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

        self.decimals_list.append(self.converter.decimal)
        self.results_list.append(result)

    def continue_menu(self):
        print("\n#########################################################################################\n")
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
        self.validate_continue_options()

    def validate_continue_options(self):

        while self.new_option not in ["1", "2", "3"]:
            print("ERRO: Por favor, insira uma opcao valida")
            self.option = str(input("Opcao escolhida: "))

        if self.new_option == "1":
            self.main_menu_options()
        elif self.new_option == "2":
            self.main_menu()
        else:
            print(f"\nObrigado por escolher a R2D2 Numeric Base Converter, {self.user.user_name}!")
            print("Abaixo, segue uma relação dos numeros que voce converteu:")
            conversion_dict = dict(zip(self.decimals_list, self.results_list))
            print(tabulate(conversion_dict.items(), headers=["DECIMAL", "CONVERSAO"]))

    def main_menu_options(self):

        if self.option == "1":
            print("\nOpcao escolhida: 1 - Conversao binaria")
            print("Otimo! Por favor, digite um numero decimal inteiro para a conversao\n")
            self.get_decimal_number()

            print("\nConvertendo numero para binario...")
            self.converter.binary = self.converter.to_binary()

            self.print_result()
            self.continue_menu()

        elif self.option == "2":
            print("\nOpcao escolhida: 2 - Conversao octodecimal")
            print("Otimo! Por favor, digite um numero decimal inteiro para a conversao\n")
            self.get_decimal_number()

            print("\nConvertendo numero para base octodecimal...")
            self.converter.octal = self.converter.to_octodecimal()

            self.print_result()
            self.continue_menu()

        elif self.option == "3":
            print("\nOpcao escolhida: 3 - Conversao hexadecimal")
            print("Otimo! Por favor, digite um numero decimal inteiro para a conversao\n")
            self.get_decimal_number()

            print("\nConvertendo numero para hexadecimal...")
            self.converter.hexal = self.converter.to_hexadecimal()

            self.print_result()
            self.continue_menu()
