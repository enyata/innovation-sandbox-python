from relianceHMO.enrollees import Enrollees

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "page": 1,
    "limit": 10
}

result = Enrollees(header).GetAllEnrollee(params)

print(result)