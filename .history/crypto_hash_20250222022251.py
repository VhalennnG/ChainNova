import hashlib
import json

def stringify(data):
  return json.dumps(data)

def crypto_hash(*args):
  """
  Return a sha-256
  """
  stringify_args = sorted(map(stringify, args))
  joined_data = ''.join(stringify_args)
  
  return hashlib.sha256(joined_data.encode('UTF-8')).hexdigest
  
def main():
  print(f"crypto_hash - {crypto_hash('one', 323, ['three'])}")
  print(f"crypto_hash - {crypto_hash(323, 'one', ['three'])}")
  
if __name__ == '__main__':
  main()