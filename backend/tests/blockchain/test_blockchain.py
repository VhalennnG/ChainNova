import pytest

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
  
@pytest.fixture
def blockchain_three_blocks():
  blockchain = Blockchain()
  for i in range(3):
    blockchain.add_block(i)
  return blockchain
  

def test_is_valid_chain(blockchain_three_blocks):
  Blockchain.is_valid_chain(blockchain_three_blocks.chain)
  
def test_is_valid_chain_bad_genesis(blockchain_three_blocks):
  blockchain_three_blocks.chain[0].hash = 'evil_hash'
  
  with pytest.raises(Exception, match="genesis block must be valid"):
    Blockchain.is_valid_chain(blockchain_three_blocks.chain)
    
def test_replace_chain(blockchain_three_blocks):
  blockchain = Blockchain()
  blockchain.replace_chain(blockchain_three_blocks.chain)
  
  assert blockchain.chain == blockchain_three_blocks.chain