from .base import IntegerPlugin


class DoubleBondStereoisomers(IntegerPlugin):
    """Number of double bond stereoisomers"""
    name = "doublebondstereoisomercount"
    default_result_keys = ["double_bond_stereoisomers"]


class Stereoisomers(IntegerPlugin):
    """Number of stereoisomers"""
    name = "stereoisomercount"
    default_result_keys = ["stereoisomers"]


class Tautomers(IntegerPlugin):
    """Number of dominant tautomers at pH=7.4"""
    name = "tautomercount"
    default_options = "-H 7.4"
    default_result_keys = ["tautomers"]


class TetrahedralStereoisomers(IntegerPlugin):
    """Number of tetrahedral stereoisomers"""
    name = "tetrahedralstereoisomercount"
    default_result_keys = ["tetrahedral_stereoisomers"]
