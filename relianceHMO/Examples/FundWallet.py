from relianceHMO.wallet import Wallet

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "amount": '250000'
}

result = Wallet(header).FundWallet(body)

print(result)
