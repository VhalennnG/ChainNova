  class Block:
  """
  Block: a unit of storage.
  Store transaction in a blockchain that supports a cryptocurrency.
  """
  def __init__(self, data):
    self.data = data
    # self.hash = hash
    
  def __repr__(self):
    return f"Block data - {self.data}"