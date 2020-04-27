from relianceHMO.utilities import Utilities

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "plan": 25
}

result = Utilities(header).Benefits(params)

print(result)
