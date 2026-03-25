
from pathlib import Path
from qiskit import qpy
BASE_DIR = Path(__file__).resolve().parent.parent
CIRCUIT_DIR= BASE_DIR / "circuits"

from qiskit import QuantumCircuit

# MAKE YOUR CIRCUIT HERE!
qc = QuantumCircuit(1,1)
qc.h(0) 
qc.measure_all()
circuit_name = "1-Bit Hadamard"
with open(CIRCUIT_DIR / (circuit_name + ".qpy"), "wb") as file:
    qpy.dump(qc, file)


