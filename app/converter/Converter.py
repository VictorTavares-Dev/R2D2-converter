from app.config import HEX_CONVERTER_DICT


class Converter:
    """
    A class to represent a numeric base converter for integer decimal numbers.

    Attributes
    ----------
    decimal: int
        the decimal number to be converted to another numeric base.
    binary: str
        the binary number resultant of the conversion.
    octal: str
        the octodecimal number resultant of the conversion.
    hexal: str
        the hexadecimal number resultant of the conversion.

    Methods
    -------
    base_converter(): str
        base converter to convert a decimal number to a binary, octodecimal or hexadecimal number, based on the value
        of the 'base' parameter.
    to_binary(): void
        method to call the base_converter() with base '2' parameter for binary conversion.
    to_octodecimal(): void
        method to call the base_converter() with base '8' parameter for octodecimal conversion.
    to_hexadecimal(): void
        method to call the base_converter() with base '16' parameter for hexadecimal conversion.
    """
    def __init__(self, decimal=None, binary=None, octal=None, hexal=None):
        self.decimal = decimal
        self.binary = binary
        self.octal = octal
        self.hexal = hexal

    def base_converter(self, base):
        """
        Uses a base parameter to covert decimal numbers to its corresponding numeric base conversion.

        Parameters
        ----------
            base : int
                represents the numeric base in which a decimal number is to be converted ('2' - binary, '8' - octodecimal
                and '16' - hexadecimal).

        Returns
        -------
            self.binary | self.octal | self.hexal: str
                the result of the conversion based on the 'base' parameter.

        """
        remainders_list = []
        decimal_number = self.decimal

        if base == 2:
            self.binary = ''
        elif base == 8:
            self.octal = ''
        elif base == 16:
            self.hexal = ''

        while decimal_number > 1:
            remainder = decimal_number % base
            remainders_list.append(remainder)
            decimal_number = decimal_number // base
        else:
            if decimal_number == 1:
                remainders_list.append(decimal_number)

        remainders_list.reverse()

        for item in remainders_list:
            if item >= 10 and base == 16:
                item = HEX_CONVERTER_DICT.get(f'{item}')

            if base == 2:
                self.binary += str(item)
            elif base == 8:
                self.octal += str(item)
            elif base == 16:
                self.hexal += str(item)

        if base == 2:
            return self.binary
        elif base == 8:
            return self.octal
        elif base == 16:
            return self.hexal

    def to_binary(self):
        """
        Calls base converter to execute binary conversion.

        Parameters
        ----------
            None.

        Returns
        -------
            result: str
                the result of the decimal to binary conversion.
        """
        result = self.base_converter(2)
        return result

    def to_octodecimal(self):
        """
        Calls base converter to execute octodecimal conversion.

        Parameters
        ----------
            None.

        Returns
        -------
            result: str
                the result of the decimal to octodecimal conversion.
        """
        result = self.base_converter(8)
        return result

    def to_hexadecimal(self):
        """
        Calls base converter to execute hexadecimal conversion.

        Parameters
        ----------
            None.

        Returns
        -------
            result: str
                the result of the decimal to hexadecimal conversion.
        """
        result = self.base_converter(16)
        return result
