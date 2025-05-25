from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
  # It should create the same hash with arguments of different data types
  # in any order
  assert crypto_hash(1, [2], 'three') == crypto_hash('three', [2], 1)
  assert crypto_hash('test cypto') == '640b48579b37fef9ea8ce73662da9a354a32ef2344d71c3a8428746ad47745e9'