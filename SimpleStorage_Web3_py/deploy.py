from solcx import compile_standard
import json
from web3 import Web3
import os

# from solcx import install_solc

# install_solc("0.6.0")

with open("./SimpleStorage.sol", "r") as file:
    contract_code = file.read()

# Compile
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage": {"content": contract_code}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

with open("SimpleStorage.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage"]["Storage"]["evm"]["bytecode"][
    "object"
]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage"]["Storage"]["abi"]

# for connecting to ganache

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = w3.eth.accounts[0]
private_key = os.getenv("PRIVATE_KEY")

# create the contract in python
contract = w3.eth.contract(abi=abi, bytecode=bytecode)
# Get latest transaction
nonce = w3.eth.getTransactionCount(my_address)
# Build the transaction
txn = contract.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)
# Sign the transaction
signed = w3.eth.account.signTransaction(txn, private_key=private_key)
print("Deploying Contract...")
# Send the transaction
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print("Deployed")
# Working with the contract, you need:
# 1. Contract address
# 2. Contract instance
# 3. Contract functions

contract_instance = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(contract_instance.functions.get().call())
print("Updaing contract....")

store_txn = contract_instance.functions.set(42).buildTransaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce + 1,
    }
)
signed_store_txn = w3.eth.account.signTransaction(store_txn, private_key=private_key)

send_store_tx = w3.eth.sendRawTransaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.waitForTransactionReceipt(send_store_tx)
print("Updated!")
print(contract_instance.functions.get().call())
