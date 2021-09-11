from brownie import accounts, config
import os


def deploy_simple_storage():
    account = accounts.add(config["wallets"]["from_key"])
    print(account)


def main():
    deploy_simple_storage()
