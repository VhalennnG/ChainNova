from backend.blockchain.block import Block

class Blockchain:
  """
  Blockchain: a public ledger of transaction.
  Implemented as a list of blocks - data sets of transactions
  """
  
  def __init__(self):
    self.chain = [Block.genesis()]
    # self.
    
  def add_block(self, data):
    last_block = self.chain[-1]
    self.chain.append(Block.mine_block(last_block, data))
    
  def __repr__(self):
    return f'Blockchain : {self.chain}'
    
  def replace_chain(self, chain):
    """
    Replace the local chain with the incoming one if the following aplies:
      - The incoming chain is longer than the local one.
      - the incoming chain is formatted properly. 
    """
    if len(chain) <= len(self.chain):
      raise Exception('Cannot replace. The incoming chain must be longer.')
    
    try:
      Blockchain.is_valid_chain(chain)
    except Exception as e:
      raise Exception(f'Cannot replace. The Incoming chain is invalid: {e}')
      
    self.chain = chain
    
    
  @staticmethod
  def is_valid_chain(chain):
    """
    Validate the incoming chain.
    Enforce the following rules of the blockchain:
      - the chain must start with the genesis block
      - block must be formatted correctly
    """
    if chain[0] != Block.genesis():
      raise Exception('The genesis block must be valid')
      
    for i in range(1, len(chain)):
      block = chain[i]
      last_block = chain[i - 1]
      Block.is_valid_block(last_block, block)
    
    
def main():
  blockchain = Blockchain()
  blockchain.add_block('einz')
  blockchain.add_block('zwei')
  blockchain.add_block('drei')
  
  print(blockchain)
  print(f"blockchain.py __name__: {__name__}")
  
if __name__ == '__main__':
  main()