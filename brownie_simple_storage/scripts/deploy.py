from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print("SimpleStorage:", simple_storage)


def main():
    deploy_simple_storage()
