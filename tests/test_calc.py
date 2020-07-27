import pytest
from cxcalc import CollectCalculator
from cxcalc.plugins import ExactMass, Mass, Name


@pytest.mark.parametrize(
    "smiles,exact_mass,mass", [
        ("N1C2C=C(C=CC=2OC(C)C1=O)NC(COC1=CC=C(C(C)=C1)C)=O", 340.14, 340.38),
        ("C12N(C)C(=CC=1C(N1C=C(C)C=CC1=N2)=O)C(=O)NC1C=CC=CC=1C", 346.14, 346.39),
    ]
)
def test_mass_calc_from_smiles(smiles, exact_mass, mass):
    calc = CollectCalculator(plugins=[ExactMass(), Mass()])
    calc.setup_logger()
    calc.run([smiles])
    properties = calc.get_data()[0]
    print(properties)
    assert round(properties['exact_mass'], 2) == exact_mass
    assert round(properties['mass'], 2) == mass



@pytest.mark.parametrize(
    "smiles,iupac_name", [
        (
            "C12N(C)C(=CC=1C(N1C=C(C)C=CC1=N2)=O)C(=O)NC1C=CC=CC=1C",
            "6,12-dimethyl-N-(2-methylphenyl)-2-oxo-1,6,8-triazatricyclo[7.4.0.0^{3,7}]trideca-3(7),4,8,10,12-pentaene-5-carboxamide"
        ),
    ]
)
def test_name_calc_from_smiles(smiles, iupac_name):
    calc = CollectCalculator(plugins=[Name()])
    calc.setup_logger()
    calc.run([smiles])
    properties = calc.get_data()[0]
    print(properties)
    assert properties['iupac_name'] == iupac_name
