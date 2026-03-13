import json
from pathlib import Path

# To connect to Lagrange
from iqm.qiskit_iqm import IQMProvider

# To build the test circuit
from qiskit import QuantumCircuit
from qiskit import transpile

# This points to the folder containing this file
BASE_DIR = Path(__file__).resolve().parent
TOKEN_PATH = BASE_DIR / 'tokens.json'

# Extract the api token
with open(TOKEN_PATH) as f:
    d = json.load(f)
api_token = d['access_token']

# Try and access Lagrange
iqm_url = "https://spark.quantum.linksfoundation.com/"
quantum_computer = "default"
provider = IQMProvider(iqm_url, quantum_computer=quantum_computer, token = api_token)
backend = provider.get_backend()

# Build a test circuit and transpile it
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.measure([0,1],[0,1])
transpiled_circuit = transpile(circuit, backend=backend)

# Send the circuit to Lagrange
job = backend.run([transpiled_circuit], shots=1024)

# Print the results
counts = job.result().get_counts()
print(counts)