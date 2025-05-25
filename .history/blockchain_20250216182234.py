class Block:
  """
  Block: a unit of storage.
  Store transaction in a blockchain that supports a cryptocurrency.
  """
  def __init__(self, data):
    self.data = data
    # self.hash = hash

class Blockchain:
  """
  Blockchain: a public ledger of transaction.
  Implemented as a list of blocks - data sets of transactions
  """
  
  def __init__(self):
    self.chain = []
    # self.
    
  def add_block(self, data):
    self.chain.append(Block(data))