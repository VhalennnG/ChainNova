import hashlib
import json

def crypto_hash(*args):
  """
  Return a sha-256
  """
  # stringify_data = json.dumps(data)
  print(f'args: {args}')
  joined_data = ''.join(args)
  print(f'joined_data: {joined_data}')
  
  return hashlib.sha256(joined_data.encode('UTF-8')).hexdigest
  
def main():
  print(f"sha - {crypto_hash('one', 'two', 'three')}")
  
if __name__ == '__main__':
  main()