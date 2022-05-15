from app.converter.Converter import Converter
from app.log.Logger import Logger


def test_success_base_converter_base_2():
    converter = Converter(logger=Logger())
    converter.decimal = 123456
    expected_result = "11110001001000000"
    actual_result = converter.base_converter(2)
    assert expected_result == actual_result


def test_success_base_converter_base_8():
    converter = Converter(logger=Logger())
    converter.decimal = 123456
    expected_result = "361100"
    actual_result = converter.base_converter(8)
    assert expected_result == actual_result


def test_success_base_converter_base_16():
    converter = Converter(logger=Logger())
    converter.decimal = 123456
    expected_result = "1E240"
    actual_result = converter.base_converter(16)
    assert expected_result == actual_result


def test_success_to_binary():
    converter = Converter(logger=Logger())
    converter.decimal = 123456
    expected_result = "11110001001000000"
    actual_result = converter.to_binary()
    assert expected_result == actual_result


def test_success_to_octodecimal():
    converter = Converter(logger=Logger())
    converter.decimal = 123456
    expected_result = "361100"
    actual_result = converter.to_octodecimal()
    assert expected_result == actual_result


def test_success_to_hexadecimal():
    converter = Converter(logger=Logger())
    converter.decimal = 123456
    expected_result = "1E240"
    actual_result = converter.to_hexadecimal()
    assert expected_result == actual_result

