from relianceHMO.plans import Plans

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "type": 'individual',
    "package": 'corporate'
}

result = Plans(header).GetAllPlans(params)

print(result)