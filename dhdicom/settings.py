from pathlib import Path

BASE = Path('.').absolute()

# Anonimizacion
EPR_TO_HIDE = ["PatientID", "PatientName"]
RECIPE_FILE = str(BASE / 'recipes/confidential')
