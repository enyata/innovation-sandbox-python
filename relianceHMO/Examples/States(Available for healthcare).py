from relianceHMO.utilities import Utilities

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

result = Utilities(header).States()

print(result)
