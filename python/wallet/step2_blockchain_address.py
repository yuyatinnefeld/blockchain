import base58
import binascii
import codecs
import hashlib

from ecdsa import NIST256p
from ecdsa import SigningKey


class Wallet(object):
    def __init__(self):
        self._private_key = SigningKey.generate(curve=NIST256p)
        self._public_key = self._private_key.get_verifying_key()
        self._blockchain_address = self.generate_blockchain_address()
    
    @property
    def private_key(self):
        return self._private_key.to_string().hex()
    
    @property
    def public_key(self):
        return self._public_key.to_string().hex()
    
    @property
    def blockchain_address(self):
        return self._blockchain_address

    def generate_blockchain_address(self):
        # step2 SHA-256 for the public key
        # step3 Ripemd160 for the SHA-256
        # step4 add network byte
        # step5 double SHA-256
        # step6 get checksum
        # step7 concatenate public key and checksum
        # step8 encode the key with Base58
    
        #2
        public_key_byte = self._public_key.to_string()
        sha256_bpk = hashlib.sha256(public_key_byte)
        sha256_bpk_digest = sha256_bpk.digest()
        #3
        ripemed160_bpk = hashlib.new('ripemd160')
        ripemed160_bpk.update(sha256_bpk_digest)
        ripemed160_bpk_digest = ripemed160_bpk.digest()
        ripemed160_bpk_hex = codecs.encode(ripemed160_bpk_digest, 'hex')
        #4
        network_byte = b'00'
        network_bitcoin_public_key = network_byte + ripemed160_bpk_hex
        network_bitcoin_public_key_bytes = codecs.decode(
            network_bitcoin_public_key, 'hex'
        )
        #5
        sha256_bpk = hashlib.sha256(network_bitcoin_public_key_bytes)
        sha256_bpk_digest = sha256_bpk.digest()
        sha256_2_nbpk = hashlib.sha256(sha256_bpk_digest)
        sha256_2_nbpk_digest = sha256_2_nbpk.digest()
        sha256_hex = codecs.encode(sha256_2_nbpk_digest, 'hex')
        #6
        checksum = sha256_hex[:8]
        #7
        address_hex = (network_bitcoin_public_key + checksum).decode('utf-8')
        #8
        blockchain_address = base58.b58encode(binascii.unhexlify(address_hex)).decode('utf-8')
        
        return blockchain_address


if __name__ == '__main__':
    wallet = Wallet()
    print("private_key: ", wallet.private_key)
    print("public_key: ", wallet.public_key)
    print("blockchain address: ",wallet.blockchain_address)


