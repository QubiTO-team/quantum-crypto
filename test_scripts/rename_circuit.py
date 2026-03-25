import sys
from pathlib import Path
import os
import json
BASE_DIR = Path(__file__).resolve().parent.parent
TOKEN_PATH = BASE_DIR / 'tokens.json'
DATA_DIR = BASE_DIR / "quantum_random_number_generation" / "data"
TEST_SCRIPT_DIR = BASE_DIR / "sp800_22_tests"
CIRCUIT_FOLDER = BASE_DIR / "circuits"
if(len(sys.argv) != 3):
    print("Usage: rename_circuit.py <old_name> <new_name>")
    exit()
renamed_json = 0 

if(not(Path.exists(CIRCUIT_FOLDER / (sys.argv[1] + ".qpy")))):
    print("Cannot rename, circuit not found.\n\nAvailable list of circuits:" )
    for filename in os.listdir(CIRCUIT_FOLDER):
        print(filename.split(".")[0])
    exit()
os.rename(CIRCUIT_FOLDER / (sys.argv[1] + ".qpy" ), CIRCUIT_FOLDER / (sys.argv[2] + ".qpy"))

for filename in os.listdir(DATA_DIR):
    data = {}
    to_rename = 0
    with open(DATA_DIR / filename, "r") as f:
        data = json.load(f)
        if(data["Circuit_Name"] == sys.argv[1]):
            to_rename = 1
    if(to_rename):
        with open(DATA_DIR / filename, "w") as f:
            data["Circuit_Name"] = sys.argv[2]
            json.dump(data, f)
        print("Renamed:", DATA_DIR/filename)
        renamed_json += 1
print("Renamed the circuit in", renamed_json, "files.")

