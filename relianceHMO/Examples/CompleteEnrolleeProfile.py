from relianceHMO.enrollees import Enrollees

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "sex": 'm',
    "date_of_birth": '1991-03-03',
    'home_address': "85, outer space",
    'has_smartphone': True,
    'profile_picture_filename': 'ttffddzp.png',
    'hash': 'ZDZhMTlYxRkQ0ODRDNisrMzQ'
}

result = Enrollees(header).Profile(body)

print(result)
