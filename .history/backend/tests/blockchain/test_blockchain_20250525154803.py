from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import Block, GENESIS_DATA

def test_blockchain():
  blockchain = Blockchain()
  assert blockchain.chain[0].hash == GENESIS_DATA['hash']
  
def test_add_block():
  blockchain = Blockchain()
  data = 'test-data'
  blockchain.add_block(data)
  
  assert blockchain.chain[-1].data == data
  
def test_is_valid_chain():
  blockchain = Blockchain()
  for i in range(3):
    blockchain.add_block(i)
    
  Blockchain.is_valid_chain(blockchain.chain)