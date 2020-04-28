from relianceHMO.enrollees import Enrollees

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "hmo_id": 'TXT/10002/A'
}

result = Enrollees(header).GetEnrollee(params)

print(result)
