from relianceHMO.utilities import Utilities

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "state": "NG-LA",
    "plan_id": 25,
    "tiers": 1,
    "page": 1,
    "limit": 50
}


result = Utilities(header).Providers(params)

print(result)
