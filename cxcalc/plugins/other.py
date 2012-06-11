from .base import FloatPlugin, IntegerPlugin


class HBondAcceptors(IntegerPlugin):
    """Number of hydrogen bond acceptor atoms"""
    name = "acceptorcount"
    default_result_keys = ["h_bond_acceptors"]


class HBondAcceptorsPH74(HBondAcceptors):
    """Number of hydrogen bond acceptor atoms of the major
    microspecies at pH=7.4"""
    default_result_keys = ["h_bond_acceptors_ph74"]
    default_options = "-H 7.4"


class HBondAcceptorSites(IntegerPlugin):
    """Number of hydrogen bond acceptor sites"""
    name = "acceptorsitecount"
    default_result_keys = ["h_bond_acceptor_sites"]


class HBondAcceptorSitesPH74(HBondAcceptorSites):
    """Number of hydrogen bond acceptor sites of the major microspecies
    at pH=7.4"""
    default_result_keys = ["h_bond_acceptor_sites_ph74"]
    default_options = "-H 7.4"


class HBondDonors(IntegerPlugin):
    """Number of hydrogen bond donor atoms"""
    name = "donorcount"
    default_result_keys = ["h_bond_donors"]


class HBondDonorsPH74(HBondDonors):
    """Number of hydrogen bond donor atoms of the major microspecies
    at pH=7.4"""
    default_result_keys = ["h_bond_donors_ph74"]
    default_options = "-H 7.4"


class HBondDonorSites(IntegerPlugin):
    """Number of hydrogen bond donor sites"""
    name = "donorsitecount"
    default_result_keys = ["h_bond_donor_sites"]


class HBondDonorSitesPH74(HBondDonorSites):
    """Number of hydrogen bond donor sites of the major microspecies
    at pH=7.4"""
    default_result_keys = ["h_bond_donor_sites_ph74"]
    default_options = "-H 7.4"


class HMOPiEnergy(FloatPlugin):
    """Pi energy of the aromatic ring(s) (dimension beta)"""
    name = "hmopienergy"
    default_result_keys = ["hmo_pi_energy"]


class HMOPiEnergyPH74(HMOPiEnergy):
    """Pi energy of the aromatic ring(s) (dimension beta) of the major
    microspecies at pH=7.4"""
    default_result_keys = ["hmo_pi_energy_ph74"]
    default_options = "-H 7.4"


class Refractivity(FloatPlugin):
    """Molar refractivity"""
    name = "refractivity"
    default_result_keys = ["refractivity"]


class Resonants(IntegerPlugin):
    """Number of resonance structures"""
    name = "resonantcount"
    default_result_keys = ["resonants"]
