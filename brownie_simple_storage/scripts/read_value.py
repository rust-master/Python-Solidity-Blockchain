from brownie import SimpleStorage, accounts, config


def read_contract():
    contract = SimpleStorage[-1]
    print(contract.get())


def main():
    read_contract()
