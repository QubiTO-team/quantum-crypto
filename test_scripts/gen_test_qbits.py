import json
from pathlib import Path
import sys
# To connect to Lagrange
from iqm.qiskit_iqm import IQMProvider
# To build the test circuit from qiskit import QuantumCircuit from qiskit import transpile
from qiskit import QuantumCircuit, transpile, qpy
import subprocess
import os
from bitarray import bitarray
import base64
# This points to the folder containing this file
if len(sys.argv) != 3 or sys.argv[1].isdigit() == 0:
    print("Usage: gen_test_qbits.py <n_shots> <circuit_name>")
    exit()

BASE_DIR = Path(__file__).resolve().parent.parent
TOKEN_PATH = BASE_DIR / 'tokens.json'
DATA_DIR = BASE_DIR / "quantum_random_number_generation" / "data"
TEST_SCRIPT_DIR = BASE_DIR / "sp800_22_tests"
CIRCUIT_FOLDER = BASE_DIR / "circuits"

sys.path.append(str(TEST_SCRIPT_DIR))
from sp800_22_module import run_tests

# Check if the script is called properly



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
circuit = QuantumCircuit(1)
with open(CIRCUIT_FOLDER / (sys.argv[2] + ".qpy"), "rb") as file:
    circuit = qpy.load(file)[0]
transpiled_circuit = transpile(circuit, backend=backend)

# Send the circuit to Lagrange

job = backend.run([transpiled_circuit], shots = int(sys.argv[1]))

# Elaborate the results
result = job.result()
bits = []
for bit in result.get_memory():
    bits.append(int(bit))


# Generate appropriate filename for storing results
filename = "Quantum_Bits-"+ sys.argv[1] 
if os.path.exists(DATA_DIR / (filename + ".json")):
    i = 1
    filename_new = filename + "-" + str(i) + ".json"
    while(os.path.exists(DATA_DIR / filename_new)):
        i+=1
        filename_new = filename + "-" + str(i) + ".json"
    filename = filename_new
else:
    filename += ".json"


result_list = run_tests(bits)
results_dict = {}
for result in result_list:
    results_dict[result[0]] = (float(result[1]), result[2])

raw_bytes = bitarray(bits).tobytes()
base64_string = base64.b64encode(raw_bytes).decode("utf-8")
data = {"Data": {"Bits": base64_string, "Bits_Encoding":"Base64", "N_Bits":len(bits)}, "Results":results_dict, "Circuit_Name":sys.argv[2]}

with open(str(DATA_DIR / filename), "w") as f:
    json.dump(data, f)
#cmd = "uv run " + str(TEST_SCRIPT_DIR / "sp800_22_tests.py") + " " + str(DATA_DIR / filename)
#subprocess.run(cmd.split(" "))
