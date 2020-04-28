from relianceHMO.consultation import Consultation

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "patient_id": 232,
    "reason": 'reason for consultation'
}

result = Consultation(header).RequestConsultation(params)

print(result)
