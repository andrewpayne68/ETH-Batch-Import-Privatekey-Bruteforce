rom web3 import Account
import web3
import os
import random
import json
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY_GOES_HERE"

w3 = web3.Web3(web3.HTTPProvider(infura_url)) # your infura api url endpoint
cracked = json.load(open("cracked.json", "r")) # (eth)store public/private key of the account found
zerobalance = json.load(open("zerobalance.json", "r")) # (no eth)store public/private key of the zero balance account

while 1:
  private_key = ''.join([random.SystemRandom().choice("0123456789abcdef") for i in range(64)])# generate random private key
  if (private_key in cracked) or (private_key in zerobalance):# make sure not a duplicate
    continue
    
  account = Account.from_key(private_key).address# convert private key to public key(address)
  balance = (w3.eth.get_balance(account))/(10**18)# get eth address balance
  
  if balance != 0: # there is eth in that account
    cracked[account] = private_key
    json.dump(cracked, open('cracked.json', 'w')) # record in cracked.json
  else:# no eth in that account
    zerobalance[account] = private_key
    json.dump(zerobalance, open('zerobalance.json', 'w')) # record in zerobalance.json

  print(f"{account}\n{private_key}")
  
