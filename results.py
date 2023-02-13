import secrets
from eth_keys import keys
import time

def results(): 
    a = 0
    while a <= 1000:
        tm = time.time() - start

        private_key = "{:064x}".format(secrets.randbits(256))
        private_key_bytes = bytes.fromhex(private_key)
        public_key_hex = keys.PrivateKey(private_key_bytes).public_key
        public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
        public_address = keys.PublicKey(public_key_bytes).to_address()

    
        print(str(a)+ "Private Key " + private_key + " Ethereum Address "+ public_address )

        result = str(a)+ "Private Key " + private_key + " Ethereum Address "+ public_address
        a = a+1
    return results

print("Total time = %s"%tm)