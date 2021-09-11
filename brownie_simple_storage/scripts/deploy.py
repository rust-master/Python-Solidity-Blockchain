from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    print("SimpleStorage:", simple_storage)
    store_value = simple_storage.get()
    print("Value:", store_value)
    transation = simple_storage.set(42, {"from": account})
    transation.wait(1)
    print("Updated Value:", simple_storage.get())


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
