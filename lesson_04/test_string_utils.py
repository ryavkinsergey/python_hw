import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("SKYPRO", "Skypro"),
    ("привет", "Привет"),
    ("123", "123")
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected


def test_capitalize_negative_none():
    with pytest.raises(AttributeError):
        utils.capitalize(None)


@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" skypro ", "skypro "),
    ("skypro", "skypro"),
    ("   ", "")
])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected


def test_trim_negative_none():
    with pytest.raises(AttributeError):
        utils.trim(None)


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("SkyPro", "", True),
    ("Sky Pro", "r", True),
    ("12345", "3", True)
])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


def test_contains_bug_empty_string():
    assert utils.contains("SkyPro", "") is True


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("яблоко", "о", "яблк"),
    ("SkyPro", "z", "SkyPro")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


def test_delete_symbol_negative_none():
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "s")
