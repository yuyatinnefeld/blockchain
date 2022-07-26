import hashlib
import json
import time

import utils
from logger import get_logger


logger = get_logger()
logger.debug('test')

class BlockChain(object):
    def __init__(self):
        self.transaction_pool  = []
        self.chain = []
        self.create_block(0, self.hash({}))
        
    def create_block(self, nonce, previous_hash):
        block = utils.sorted_dict_by_key({
            'timestamp': time.time(),
            'transactions': self.transaction_pool,
            'nonce': nonce,
            'previous_hash': previous_hash
        })
        
        self.chain.append(block)
        self.transaction_pool = []
        return block
    
    def hash(self, block):
        sorted_block = json.dumps(block, sort_keys=True)
        encoded_block = hashlib.sha256(sorted_block.encode()).hexdigest()
        return encoded_block
    
    def add_transaction(self, sender_address, recipient_address, value):
        transaction = utils.sorted_dict_by_key({
            'sender_address': sender_address,
            'recipient_address': recipient_address,
            'value': float(value)
        })
        self.transaction_pool.append(transaction)
        return True
    
def pprint(chains):
    for i, chain in enumerate(chains):
        print(f'{"="*25} Chain {i} {"="*25}')
        for k, v in chain.items():
            if k == 'transactions':
                print(k)
                for d in v:
                    print(f'{"-"*60}')
                    for kk, vv in d.items():
                        print(f'{kk:30}{vv}')
            else:
                print(f'{k:15}{v}')
            
    print(f'{"="*60}', '\n'* 2)


if __name__ == '__main__':
    block_chain = BlockChain()
    pprint(block_chain.chain)
    
    block_chain.add_transaction('YU', 'TAK', 3)
    last_block = block_chain.chain[-1]
    previous_hash = block_chain.hash(last_block)
    block_chain.create_block(20, previous_hash)
    pprint(block_chain.chain)
    
    block_chain.add_transaction('JI', 'YU', 1.4)
    block_chain.add_transaction('AN', 'YU', 4.4)
    last_block = block_chain.chain[-1]
    previous_hash = block_chain.hash(last_block)
    block_chain.create_block(5, previous_hash)    
    pprint(block_chain.chain)