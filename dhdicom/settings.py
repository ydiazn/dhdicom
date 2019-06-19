from pathlib import Path

BASE = Path(__file__).parent.absolute()

# Anonimizacion
EPR_TO_HIDE = [
    "PatientID", "PatientName", "PatientBirthDate",
    "SOP_Instance_UID", "StudyDate", "SeriesDate",
    "AcquisitionDate", "ContentDate", "AccessionNumber",
    "InstitutionName", "ReferringPhysicianName", "StationName",
    "Institutional_Department_Name", "Operators_Name", "Study_Instance_UID",
    "Series_Instance_UID", "Study_ID", "Series_Number",
    "AcquisitonNumber", "InstanceNumber"
]

RECIPE_FILE = str(BASE / 'recipes/confidential')
