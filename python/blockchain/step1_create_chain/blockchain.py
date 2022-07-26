import time

from logger import get_logger


logger = get_logger()
logger.debug('test')

class BlockChain(object):
    def __init__(self):
        self.transaction_pool  = []
        self.chain = []
        self.create_block(0, 'init hash')
        
    def create_block(self, nonce, previous_hash):
        block = {
            'timestamp': time.time(),
            'transactions': self.transaction_pool,
            'nonce': nonce,
            'previous_hash': previous_hash
        }
        
        self.chain.append(block)
        self.transaction_pool = [] #reset transaction_pool
        
        return block
    
def pprint(chains):
    for i, chain in enumerate(chains):
        print(f'{"="*25} Chain {i} {"="*25}')
        for key, val in chain.items():
            print(f'{key:15}{val}')
    print(f'{"="*60}', '\n'* 2)


if __name__ == '__main__':
    block_chain = BlockChain()
    pprint(block_chain.chain)
    block_chain.create_block(20, 'hash 1')
    pprint(block_chain.chain)
    block_chain.create_block(10, 'hash 2')
    pprint(block_chain.chain)