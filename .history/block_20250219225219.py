import time

class Block:
  """
  Block: a unit of storage.
  Store transaction in a blockchain that supports a cryptocurrency.
  """
  def __init__(self, timestamp, last_hash, hash, data):
    self.timestamp = timestamp
    self.last_hash = last_hash
    self.hash = hash
    self.data = data
    
  def __repr__(self):
    return (
      'Block: [\n'
      f"timestamp: {self.timestamp}\n"
      f"last_hash: {self.last_hash}\n"
      f"hash: {self.hash}\n"
      f"data: {self.data}\n]\n"
    )
    
  def mine_block(last_block, data):
    """"
    Mine a block based on the given last block and data
    """
    timestamp = time.time_ns()
    last_hash = last_block.hash
    hash = f'{timestamp}-{last_hash}'
    
    return Block(timestamp, last_hash, hash, data)
    
  def genesis():
    """
    Generate the genesis block
    """
    return Block(1, 'genesis_last_hash', 'genesis_hash', [])
    
def main():
  genesis_block = Block.genesis()
  block = Block.mine_block(genesis_block, 'foo')
  print(block)
  
if __name__ == '__main__':
  main()