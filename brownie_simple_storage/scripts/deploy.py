from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print("SimpleStorage:", simple_storage)
    store_value = simple_storage.get()
    print("Value:", store_value)
    transation = simple_storage.set(42, {"from": account})
    transation.wait(1)
    print("Updated Value:", simple_storage.get())


def main():
    deploy_simple_storage()
