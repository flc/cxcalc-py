# Usage

## From SMILES
```
from cxcalc import CollectCalculator
from cxcalc.contrib.lists import get_all_plugins


smiles = "N1C2C=C(C=CC=2OC(C)C1=O)NC(COC1=CC=C(C(C)=C1)C)=O"
calc = CollectCalculator(plugins=get_all_plugins())
calc.run([smiles])
properties = calc.get_data()[0]
```

## From SDF file
```
from cxcalc import CollectCalculator
from cxcalc.contrib.lists import get_all_plugins


structure = open('structure.sdf').read()
calc = CollectCalculator(plugins=get_all_plugins())
calc.run([structure])
properties = calc.get_data()[0]
```
