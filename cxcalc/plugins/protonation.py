from .base import FloatPlugin


class AvgCharge(FloatPlugin):
    """Average charge of the microspecies population (at pH=7.4 by default)"""
    name = "averagemicrospeciescharge"
    default_result_keys = ["avg_charge"]
    result_columns_num = 2  # pH is in the first column
    result_column_offset = 1


class PI(FloatPlugin):
    """pI; pH value where the net charge of an ionizable molecule is zero"""
    name = "isoelectricpoint"
    default_result_keys = ["pi"]


