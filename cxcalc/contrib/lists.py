from cxcalc.plugins import *


_partitioning_plugins = [
    LogP(),
    LogD(),
]


_protonation_plugins = [
    Pka(),
    AvgCharge(),
    PI(),
]


_name_plugins = [
    Name(),
    TraditionalName(),
]


_elemental_analysis_plugins = [
    Atoms(),
    CarbonAtoms(),
    NitrogenAtoms(),
    OxygenAtoms(), # n+o atoms also needed
    #Formula(),
    #DotDisconnectedFormula(),
    ExactMass(),
    Mass(),
]


_charge_plugins = [
    MolecularPolarizability(),
    MolecularPolarizabilityPH74(),
]


_geometry_plugins = [
    AliphaticAtoms(),
    AliphaticBonds(),
    AliphaticRings(),
    AliphaticMemberedRings(  # Aliphatic 3-membered rings
        options="-z 3",
        result_keys=["aliphatic_3_membered_rings"]
    ),
    AliphaticMemberedRings(  # Aliphatic 4-membered rings
        options="-z 4",
        result_keys=["aliphatic_4_membered_rings"]
    ),
    AliphaticMemberedRings(  # Aliphatic 5-membered rings
        options="-z 5",
        result_keys=["aliphatic_5_membered_rings"]
    ),
    AliphaticMemberedRings(  # Aliphatic 6-membered rings
        options="-z 6",
        result_keys=["aliphatic_6_membered_rings"]
    ),
    AliphaticMemberedRings(  # Aliphatic 7-membered rings
        options="-z 7",
        result_keys=["aliphatic_7_membered_rings"]
    ),
    AliphaticMemberedRings(  # Aliphatic 8-membered rings
        options="-z 8",
        result_keys=["aliphatic_8_membered_rings"]
    ),
    AromaticAtoms(),
    AromaticBonds(),
    AromaticRings(),
    AromaticMemberedRings(  # Aromatic 3-membered rings
        options="-z 3",
        result_keys=["aromatic_3_membered_rings"],
    ),
    AromaticMemberedRings(  # Aromatic 4-membered rings
        options="-z 4",
        result_keys=["aromatic_4_membered_rings"],
    ),
    AromaticMemberedRings(  # Aromatic 5-membered rings
        options="-z 5",
        result_keys=["aromatic_5_membered_rings"],
    ),
    AromaticMemberedRings(  # Aromatic 6-membered rings
        options="-z 6",
        result_keys=["aromatic_6_membered_rings"],
    ),
    AromaticMemberedRings(  # Aromatic 7-membered rings
        options="-z 7",
        result_keys=["aromatic_7_membered_rings"],
    ),
    AromaticMemberedRings(  # Aromatic 8-membered rings
        options="-z 8",
        result_keys=["aromatic_8_membered_rings"],
    ),
    ASAPH74(),
    ASA(),
    AsymmetricAtoms(),
    BalabanIndex(),
    Bonds(),
    CarbonRings(),
    AliphaticCarbonRings(),
    AromaticCarbonRings(),
    ChainAtoms(),
    ChainBonds(),
    ChiralCenters(),
    CyclomaticNumber(),
    FusedAliphaticRings(),
    FusedAromaticRings(),
    FusedRings(),
    HararyIndex(),
    HeteroAliphaticRings(),
    HyperWienerIndex(),
    LargestRingSize(),
    LargestRingSystemSize(),
    VdWSAPH74(),
    VdWSA(),
    PlattIndex(),
    PolarSurfaceAreaPH74(),
    PolarSurfaceArea(),
    RandicIndex(),
    RingAtoms(),
    RingBonds(),
    Rings(),
    MemberedRings(  # 3-membered rings
        options="-z 3",
        result_keys=["membered_rings_3"],
    ),
    MemberedRings(  # 4-membered rings
        options="-z 4",
        result_keys=["membered_rings_4"],
    ),
    MemberedRings(  # 5-membered rings
        options="-z 5",
        result_keys=["membered_rings_5"],
    ),
    MemberedRings(  # 6-membered rings
        options="-z 6",
        result_keys=["membered_rings_6"],
    ),
    MemberedRings(  # 7-membered rings
        options="-z 7",
        result_keys=["membered_rings_7"],
    ),
    MemberedRings(  # 8-membered rings
        options="-z 8",
        result_keys=["membered_rings_8"],
    ),
    RingSystems(),
    RotatableBonds(),
    SmallestRingSize(),
    SmallestRingSystemSize(),
    StereoDoubleBonds(),
    SzegedIndex(),
    WienerIndex(),
    WienerPolarity(),
]


_isomers_plugins = [
    DoubleBondStereoisomers(),
    Stereoisomers(),
    Tautomers(),
    TetrahedralStereoisomers(),
]


_other_plugins = [
    HBondAcceptors(),
    HBondAcceptorsPH74(),
    HBondAcceptorSites(),
    HBondAcceptorSitesPH74(),
    HBondDonors(),
    HBondDonorsPH74(),
    HBondDonorSites(),
    HBondDonorSitesPH74(),
    HMOPiEnergy(),
    HMOPiEnergyPH74(),
    Refractivity(),
    Resonants(),
]


_all_plugins = _partitioning_plugins[:]
_all_plugins.extend(_protonation_plugins)
_all_plugins.extend(_name_plugins)
_all_plugins.extend(_elemental_analysis_plugins)
_all_plugins.extend(_charge_plugins)
_all_plugins.extend(_geometry_plugins)
_all_plugins.extend(_isomers_plugins)
_all_plugins.extend(_other_plugins)


def get_partitioning_plugins():
    return _partitioning_plugins[:]


def get_protonation_plugins():
    return _protonation_plugins[:]


def get_name_plugins():
    return _name_plugins[:]


def get_elemental_analysis_plugins():
    return _elemental_analysis_plugins[:]


def get_charge_plugins():
    return _charge_plugins[:]


def get_geometry_plugins():
    return _geometry_plugins[:]


def get_isomers_plugins():
    return _isomers_plugins[:]


def get_other_plugins():
    return _other_plugins[:]


def get_all_plugins():
    return _all_plugins[:]

