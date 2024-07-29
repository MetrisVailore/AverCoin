from trilio import Trilio
import datetime

blockchain = Trilio()
wallet = blockchain.Wallet.create_wallet()
address = wallet["address"]
pve = address["pve"] # Private key
pbc = address["pbc"] # Public key
print(address)
print(blockchain.Wallet.get_public_key(private_key=pve))