import hashlib

def crypto_hash(data):
  """
  Return a sha-256
  """
  return hashlib.sha256(data.encode('UTF-8')).hexdigest
  
def main():
  print(f"sha - {crypto_hash('doctor')}")
  
if __name__ == '__main__':
  main()