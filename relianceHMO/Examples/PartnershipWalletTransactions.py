from relianceHMO.wallet import Wallet

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}


result = Wallet(header).PartnershipWalletTransactions()

print(result)
