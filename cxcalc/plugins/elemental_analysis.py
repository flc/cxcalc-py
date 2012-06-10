from .base import FloatPlugin, IntegerPlugin, StringPlugin


class Atoms(IntegerPlugin):
    """Number of atoms"""
    name = "atomcount"
    default_result_keys = ["atoms"]


class CarbonAtoms(Atoms):
    """Number of carbon atoms"""
    default_options = "-z 6"
    default_result_keys = ["carbon_atoms"]


class NitrogenAtoms(Atoms):
    """Number of nitrogen atoms"""
    default_options = "-z 7"
    default_result_keys = ["nitrogen_atoms"]


class OxygenAtoms(Atoms):
    """Number of oxygen atoms"""
    default_options = "-z 8"
    default_result_keys = ["oxygen_atoms"]


class Formula(StringPlugin):
    """Chemical formula according to the Hill system"""
    name = "formula"
    default_result_keys = ["formula"]


class ExactMass(FloatPlugin):
    """Monoisotopic molecule mass calculated from the atomic masses of the
    most frequent natural isotopes"""
    name = "exactmass"
    default_result_keys = ["exact_mass"]


class Mass(FloatPlugin):
    """Average molecule mass calculated from the atomic masses of all isotopes
    weighted by their natural occurrence"""
    name = "mass"
    default_result_keys = ["mass"]
