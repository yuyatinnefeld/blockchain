import hashlib
import json
import time
from wsgiref.util import guess_scheme

import utils
from logger import get_logger


MINING_DIFFICULTY = 3

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

    def valid_poof(self, transactions, previous_hash, nonce, difficulty=MINING_DIFFICULTY):
        guess_block = utils.sorted_dict_by_key({
            'transactions': transactions,
            'nonce': nonce,
            'previous_hash': previous_hash
        })
        
        guess_hash = self.hash(guess_block)
        result = guess_hash[:difficulty] == '0'*difficulty
        print("result: ",result)
        return result


    def pool_of_work(self):
        transactions = self.transaction_pool.copy()
        previous_hash = self.hash(self.chain[-1])
        nonce = 0
        while self.valid_poof(transactions, previous_hash, nonce) is False:
            nonce += 1
            print("try")
            print("nonce: ",nonce)
        return nonce
        

if __name__ == '__main__':
    block_chain = BlockChain()
    utils.pprint(block_chain.chain)
    
    block_chain.add_transaction('YU', 'TAK', 3)
    last_block = block_chain.chain[-1]
    previous_hash = block_chain.hash(last_block)
    nonce = block_chain.pool_of_work()
    block_chain.create_block(nonce, previous_hash)
    utils.pprint(block_chain.chain)
    
    block_chain.add_transaction('JI', 'YU', 1.4)
    block_chain.add_transaction('AN', 'YU', 4.4)
    last_block = block_chain.chain[-1]
    previous_hash = block_chain.hash(last_block)
    nonce = block_chain.pool_of_work()
    block_chain.create_block(nonce, previous_hash)
    utils.pprint(block_chain.chain)