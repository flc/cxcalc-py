from .base import StringPlugin


class Name(StringPlugin):
    """IUPAC name"""
    name = "name"
    default_result_keys = ["iupac_name"]


class TraditionalName(Name):
    """Traditional name"""
    default_options = "-t traditional"
    default_result_keys = ["traditional_name"]


