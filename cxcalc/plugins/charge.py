from .base import FloatPlugin


class MolecularPolarizability(FloatPlugin):
    """Molecular polarizability calculated from atomic contributions"""
    name = "molecularpolarizability"
    default_result_keys = ["molecular_polarizability"]


class MolecularPolarizabilityPH74(MolecularPolarizability):
    """Molecular polarizability of the major microspecies at pH=7.4 calculated
    from atomic contributions"""
    default_options = "-H 7.4"
    default_result_keys = ["molecular_polarizability_ph74"]


