import hashlib

def crypto_hash(data):
  """
  Return a sha-256
  """
  return hashlib.sha256(data)
  
def main():
  print(f"sha - {crypto_hash('doctor')}")