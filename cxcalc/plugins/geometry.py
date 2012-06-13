from .base import FloatPlugin, IntegerPlugin


class AliphaticAtoms(IntegerPlugin):
    """Number of aliphatic atoms"""
    name = "aliphaticatomcount"
    default_result_keys = ["aliphatic_atoms"]


class AliphaticBonds(IntegerPlugin):
    """Number of aliphatic bonds"""
    name = "aliphaticbondcount"
    default_result_keys = ["aliphatic_bonds"]


class AliphaticRings(IntegerPlugin):
    name = "aliphaticringcount"
    default_result_keys = ["aliphatic_rings"]


class AliphaticMemberedRings(IntegerPlugin):
    """Number of aliphatic N-membered rings"""
    name = "aliphaticringcountofsize"


class AromaticAtoms(IntegerPlugin):
    """Number of aromatic atoms"""
    name = "aromaticatomcount"
    default_result_keys = ["aromatic_atoms"]


class AromaticBonds(IntegerPlugin):
    """Number of aromatic bonds"""
    name = "aromaticbondcount"
    default_result_keys = ["aromatic_bonds"]


class AromaticRings(IntegerPlugin):
    """Number of aromatic rings"""
    name = "aromaticringcount"
    default_result_keys = ["aromatic_rings"]


class AromaticMemberedRings(IntegerPlugin):
    """Number of aromatic N-membered rings"""
    name = "aromaticringcountofsize"


class ASA(FloatPlugin):
    """Total solvent accessible surface area (in Angstrom2)
    of major microspecies;
    Solvent accessible surface area (in Angstrom2) of all atoms with
    positive partial charge;
    Solvent accessible surface area (in Angstrom2) of all atoms with
    negative partial charge;
    Solvent accessible surface area (in Angstrom2) of all hydrophobic
    (|qi|<0.125) atoms (|qi| is the absolute value of the partial charge
    of the atom);
    Solvent accessible surface area (in Angstrom2) of all polar (|qi|>0.125)
    atoms (|qi| is the absolute value of the partial charge of the atom);
    """
    name = "asa"
    default_result_keys = ["asa", "asa_pos", "asa_neg", "asa_h", "asa_p"]
    result_columns_num = 5


class ASAPH74(ASA):
    """Total solvent accessible surface area (in Angstrom2)
    of major microspecies at pH=7.4;
    Solvent accessible surface area (in Angstrom2) of all atoms with positive
    partial charge of major microspecies at pH=7.4;
    Solvent accessible surface area (in Angstrom2) of all atoms with negative
    partial charge of major microspecies at pH=7.4;
    Solvent accessible surface area (in Angstrom2) of all hydrophobic
    (|qi|<0.125) atoms (|qi| is the absolute value of the partial charge
    of the atom) of major microspecies at pH=7.4;
    Solvent accessible surface area (in Angstrom2) of all polar (|qi|>0.125)
    atoms (|qi| is the absolute value of the partial charge of the atom) of
    major microspecies at pH=7.4;
    """
    default_options = "-H 7.4"
    default_result_keys = ["asa_ph74", "asa_ph74_pos", "asa_ph74_neg",
                           "asa_ph74_h", "asa_ph74_p"]


class AsymmetricAtoms(IntegerPlugin):
    """Number of asymmetric atoms"""
    name = "asymmetricatomcount"
    default_result_keys = ["asymmetric_atoms"]


class BalabanIndex(FloatPlugin):
    """Balaban distance connectivity, which is the average distance
    sum connectivity"""
    # XXX 8 as value?
    name = "balabanindex"
    default_result_keys = ["balaban_index"]


class Bonds(IntegerPlugin):
    """Number of bonds including bonds of hydrogen atoms"""
    name = "bondcount"
    default_result_keys = ["bonds"]


class CarbonRings(IntegerPlugin):
    name = "carboringcount"
    default_result_keys = ["carbon_rings"]


class AliphaticCarbonRings(IntegerPlugin):
    """Number of aliphatic rings containing carbon atoms only"""
    name = "carboaliphaticringcount"
    default_result_keys = ["aliphatic_carbon_rings"]


class AromaticCarbonRings(IntegerPlugin):
    """Number of aromatic rings containing carbon atoms only"""
    name = "carboaromaticringcount"
    default_result_keys = ["aromatic_carbon_rings"]


class ChainAtoms(IntegerPlugin):
    """Number of chain atoms (non-ring atoms excluding hydrogens)"""
    name = "chainatomcount"
    default_result_keys = ["chain_atoms"]


class ChainBonds(IntegerPlugin):
    """Number of chain bonds
    (non-ring bonds excluding bonds of hydrogen atoms)"""
    name = "chainbondcount"
    default_result_keys = ["chain_bonds"]


class ChiralCenters(IntegerPlugin):
    """Number of tetrahedral stereogenic center atoms."""
    name = "chiralcentercount"
    default_result_keys = ["chiral_centers"]


class CyclomaticNumber(IntegerPlugin):
    """Smallest number of bonds which must be removed so that no circuit
    remains. Also known as circuit rank."""
    name = "cyclomaticnumber"
    default_result_keys = ["cyclomatic_number"]


class FusedAliphaticRings(IntegerPlugin):
    """Number of fused aliphatic rings"""
    name = "fusedaliphaticringcount"
    default_result_keys = ["fused_aliphatic_rings"]


class FusedAromaticRings(IntegerPlugin):
    """Number of fused aromatic rings"""
    name = "fusedaromaticringcount"
    default_result_keys = ["fused_aromatic_rings"]


class FusedRings(IntegerPlugin):
    """Number of fused rings"""
    name = "fusedringcount"
    default_result_keys = ["fused_rings"]


class HararyIndex(FloatPlugin):
    """Half-sum of the off-diagonal elements of the reciprocal
    molecular distance matrix"""
    # XXX 8 as value?
    name = "hararyindex"
    default_result_keys = ["harary_index"]


class HeteroAliphaticRings(IntegerPlugin):
    """Number of aliphatic heterocycles"""
    name = "heteroaliphaticringcount"
    default_result_keys = ["hetero_aliphatic_rings"]


class HeteroAromaticRings(IntegerPlugin):
    """Number of aromatic heterocycles"""
    name = "heteroaromaticringcount"
    default_result_keys = ["hetero_aromatic_rings"]


class HeteroRings(IntegerPlugin):
    """Number of heterocycles"""
    name = "heteroringcount"
    default_result_keys = ["hetero_rings"]


class HyperWienerIndex(FloatPlugin):
    """A variant of the Wiener index"""
    # XXX 8 as value?
    name = "hyperwienerindex"
    default_result_keys = ["hyperwienerindex"]


class LargestRingSize(IntegerPlugin):
    """Size of the largest ring"""
    name = "largestringsize"
    default_result_keys = ["largest_ring_size"]


class LargestRingSystemSize(IntegerPlugin):
    """Number of rings in the largest ring system"""
    name = "largestringsystemsize"
    default_result_keys = ["largest_ring_system_size"]


class VdWSA(FloatPlugin):
    """Van der Waals surface area"""
    name = "vdwsa"
    default_result_keys = ["vdwsa"]


class VdWSAPH74(VdWSA):
    """Van der Waals surface area of the major microspecies at pH=7.4"""
    default_options = "-H 7.4"
    default_result_keys = ["vdwsa_ph74"]


class PlattIndex(IntegerPlugin):
    """Sum of the edge degrees of a molecular graph"""
    name = "plattindex"
    default_result_keys = ["platt_index"]


class PolarSurfaceArea(FloatPlugin):
    """Topological polar surface area"""
    name = "polarsurfacearea"
    default_result_keys = ["polar_surface_area"]


class PolarSurfaceAreaPH74(PolarSurfaceArea):
    """Topological polar surface area of the major microspecies at pH=7.4"""
    default_options = "-H 7.4"
    default_result_keys = ["polar_surface_area_ph74"]


class RandicIndex(FloatPlugin):
    """Harmonic sum of the geometric means of the node degrees for each edge"""
    name = "randicindex"
    default_result_keys = ["randic_index"]


class RingAtoms(IntegerPlugin):
    """Number of ring atoms"""
    name = "ringatomcount"
    default_result_keys = ["ring_atoms"]


class RingBonds(IntegerPlugin):
    """Number of ring bonds"""
    name = "ringbondcount"
    default_result_keys = ["ring_bonds"]


class Rings(IntegerPlugin):
    """Number of rings (smallest set of smallest rings)"""
    name = "ringcount"
    default_result_keys = ["rings"]


class MemberedRings(IntegerPlugin):
    """Number of N-membered rings"""
    name = "ringcountofsize"


class RingSystems(IntegerPlugin):
    """Number of disjunct ring systems"""
    name = "ringsystemcount"
    default_result_keys = ["ring_systems"]


class RotatableBonds(IntegerPlugin):
    """Number of rotatable bonds"""
    name = "rotatablebondcount"
    default_result_keys = ["rotatable_bonds"]


class SmallestRingSize(IntegerPlugin):
    """Size of the smallest ring"""
    name = "smallestringsize"
    default_result_keys = ["smallest_ring_size"]


class SmallestRingSystemSize(IntegerPlugin):
    """Number of rings in the smallest ring system"""
    name = "smallestringsystemsize"
    default_result_keys = ["smallest_ring_system_size"]


class StereoDoubleBonds(IntegerPlugin):
    """Number of double bonds with defined stereochemistry"""
    name = "stereodoublebondcount"
    default_result_keys = ["stereo_double_bonds"]


class SzegedIndex(IntegerPlugin):
    """Wiener index extended for cyclic graphs by counting the number of atoms
    on both sides of each bond (those atoms only which are nearer to the given
    side of the bond than to the other), and sum these counts."""
    name = "szegedindex"
    default_result_keys = ["szeged_index"]


class WienerIndex(IntegerPlugin):
    """Average topological atom distance
    (half of the sum of all atom distances)"""
    # XXX 8 as value?
    name = "wienerindex"
    default_result_keys = ["wiener_index"]


class WienerPolarity(IntegerPlugin):
    """Number of 3 bond length distances"""
    # XXX 8 as value?
    name = "wienerpolarity"
    default_result_keys = ["wiener_polarity"]
